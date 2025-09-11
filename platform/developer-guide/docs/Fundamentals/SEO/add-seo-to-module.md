# Add SEO Capabilities to Module

This guide will walk you through adding SEO support to your custom module in Virto Commerce. You'll modify the backend, xAPI, and frontend to display semantic URLs and inject SEO metadata dynamically.

## Backend (database and UI)

This section shows how to add a new SEO entity to your module's database model and UI, including necessary relationships and widget registration:

1. In the backend **.Data** project:

    1. Add a SEO entity: 

        ```csharp
        public class SeoInfoEntity : AuditableEntity, IDataEntity<SeoInfoEntity, SeoInfo>
        {
            [Required]
            [StringLength(IdLength)]
            public string NewsArticleId { get; set; }//FK to your entity

            [StringLength(IdLength)]
            public string StoreId { get; set; }

            [StringLength(Length256)]
            [Required]
            public string Keyword { get; set; }

            public bool IsActive { get; set; }

            [StringLength(CultureNameLength)]
            public string LanguageCode { get; set; }

            [StringLength(Length256)]
            public string Title { get; set; }

            [StringLength(Length1024)]
            public string MetaDescription { get; set; }

            [StringLength(Length256)]
            public string MetaKeywords { get; set; }

            [StringLength(Length256)]
            public string ImageAltDescription { get; set; }

            public virtual NewsArticleEntity NewsArticle { get; set; }//Navigation property to your entity
            
            public virtual SeoInfo ToModel(SeoInfo seoInfo)
            {
                seoInfo.Id = Id;
                seoInfo.CreatedBy = CreatedBy;
                seoInfo.CreatedDate = CreatedDate;
                seoInfo.ModifiedBy = ModifiedBy;
                seoInfo.ModifiedDate = ModifiedDate;

                seoInfo.LanguageCode = LanguageCode;
                seoInfo.SemanticUrl = Keyword;
                seoInfo.PageTitle = Title;
                seoInfo.ImageAltDescription = ImageAltDescription;
                seoInfo.IsActive = IsActive;
                seoInfo.MetaDescription = MetaDescription;
                seoInfo.MetaKeywords = MetaKeywords;
                seoInfo.ObjectId = NewsArticleId;
                seoInfo.ObjectType = nameof(NewsArticle);//Note this field
                seoInfo.StoreId = StoreId;

                return seoInfo;
            }
            //Other IDataEntity methods implementation omitted
        }
        ```

    1. Create necessary migrations. 
    1. Make changes to your Repository classes:

        ```csharp
        public class NewsArticleEntity : AuditableEntity, IDataEntity<NewsArticleEntity, NewsArticle>
        {
            //IDataEntity implementation and properties omitted
            
            public virtual ObservableCollection<SeoInfoEntity> SeoInfos { get; set; } = new NullCollection<SeoInfoEntity>();
        }
        ```
 

1. Implement **ISeoSupport** in your **.Core** project model:

    ```csharp
    public class NewsArticle : AuditableEntity, ICloneable, ISeoSupport
    {
        //Other properties omitted
        
        public IList<SeoInfo> SeoInfos { get; set; }
        
        public object Clone()
        {
            var result = (NewsArticle)MemberwiseClone();

            result.SeoInfos = SeoInfos?.Select(x => x.CloneTyped()).ToList();

            return result;
        }
    }
    ```

1. Add a SEO widget to your blade in the **.Web** project:

    ```csharp
            var seoWidget = {
                controller: 'virtoCommerce.coreModule.seo.seoWidgetController',
                template: 'Modules/$(VirtoCommerce.Core)/Scripts/SEO/widgets/seoWidget.tpl.html',
                objectType: 'NewsArticle',
                getDefaultContainerId: function (blade) { return undefined; },
                getLanguages: function (blade) { return blade.languages; }
            };
            widgetService.registerWidget(seoWidget, 'newsArticleDetails');
    ```


Now your backend UI should look like this:

![SEO widget](media/seo-widget.png)

Test it to make sure everything works as expected.

## xAPI

This section explains how to expose SEO data via GraphQL and filter it correctly server-side.

1. Add SEO data to the return type of your xAPI:

    ```csharp 
    public class NewsArticleContentType : ExtendableGraphType<NewsArticle>
    {
        public NewsArticleContentType()
        { 
            //Other fields omitted
            
            ExtendableField<NonNullGraphType<SeoInfoType>>("seoInfo", resolve: context => context.Source.SeoInfos.FirstOrDefault());
        }
    }
    ```

1. It is recommended to return only one `“seoInfo”` item per object to avoid client-side filtration. You can implement some basic server-side filtration in the GraphQL type, but sometimes is better to put it in the **QueryHandler** or even create a separate **Service**:

    ```csharp
    public class NewsArticlesQueryHandler() : IQueryHandler<NewsArticleQuery, NewsArticle>, IQueryHandler<NewsArticlesQuery, NewsArticleSearchResult>
    {
        public async Task<NewsArticle> Handle(NewsArticleQuery request, CancellationToken cancellationToken)
        {
            var result = await newsArticleService.GetNoCloneAsync(request.Id);

            if (result != null)
            {
                await PostProcessResultAsync(request.StoreId, request.LanguageCode, [result]);
            }

            return result;
        }

        public async Task<NewsArticleSearchResult> Handle(NewsArticlesQuery request, CancellationToken cancellationToken)
        {
            var searchCriteria = await BuildSearchCriteria(request);

            var result = await newsArticleSearchService.SearchAsync(searchCriteria);

            if (!result.Results.IsNullOrEmpty())
            {
                await PostProcessResultAsync(request.StoreId, request.LanguageCode, result.Results);
            }

            return result;
        }

        protected virtual async Task PostProcessResultAsync(string storeId, string languageCode, IList<NewsArticle> newsArticles)
        {
            var store = !storeId.IsNullOrEmpty() ? await storeService.GetNoCloneAsync(storeId) : null;
            
            await FilterSeoInfosAsync(newsArticles, languageCode, storeId, store?.DefaultLanguage);
        }

        protected virtual Task FilterSeoInfosAsync(IList<NewsArticle> newsArticles, string languageCode, string storeId, string storeDefaultLanguage)
        {
            foreach (var newsArticle in newsArticles)
            {
                SeoInfo seoInfo = null;
                var activeSeoInfos = newsArticle.SeoInfos?.Where(x => x.IsActive).ToList();

                if (!activeSeoInfos.IsNullOrEmpty())
                {
                    seoInfo = activeSeoInfos.GetBestMatchingSeoInfo(storeId, storeDefaultLanguage, languageCode);
                }

                if (seoInfo == null)
                {
                    seoInfo = SeoExtensions.GetFallbackSeoInfo(newsArticle.Id, newsArticle.Name, languageCode);
                }

                newsArticle.SeoInfos.Clear();
                newsArticle.SeoInfos.Add(seoInfo);
            }

            return Task.CompletedTask;
        }
    }
    ```

Now, you can query the SEO data and test your xAPI:

![GrqphiQL](media/graphiql.png)


## Frontend - page meta and open graph

This section demonstrates how to use GraphQL SEO fields to inject meta tags into your Vue app for Open Graph and search engines:

1. Add SEO fields to your query **.graphql** files and regenerate the types (run `yarn generate:graphql-types` in terminal):

    ```graphql
    query NewsArticle($id: String!, $storeId: String!, $languageCode: String!) {
      newsArticle(id: $id, storeId: $storeId, languageCode: $languageCode) {
        id
        title
        publishDate
        content
        contentPreview
        seoInfo {
        pageTitle
        metaKeywords
        metaDescription
        semanticUrl
        }
      }
    }
    ```

1. To apply SEO metadata to your entity page, add to following lines to your **.vue** page.  

    ```csharp
    <script lang="ts" setup>
    import { useSeoMeta } from "@unhead/vue";
    import { usePageTitle } from "@/core/composables";

    const newsArticle = ref<NewsArticleContent>();//Fetching is omitted

    const seoTitle = computed(() => newsArticle.value?.seoInfo?.pageTitle || newsArticle.value?.title);
    const { title: pageTitle } = usePageTitle(seoTitle);

    const seoDescription = computed(() => newsArticle.value?.seoInfo?.metaDescription);
    const seoKeywords = computed(() => newsArticle.value?.seoInfo?.metaKeywords);

    const seoUrl = computed(() =>
      newsArticle.value?.seoInfo?.semanticUrl
        ? `${window.location.host}/news/${newsArticle.value?.seoInfo?.semanticUrl}`
        : window.location.toString(),
    );

    useSeoMeta({
      title: () => pageTitle.value,
      keywords: () => seoKeywords.value,
      description: () => seoDescription.value,
      ogUrl: () => seoUrl.value,
      ogTitle: () => pageTitle.value,
      ogDescription: () => seoDescription.value,
      ogType: () => "website",
    });
    </script>
    ```


1. After opening your object page the title should change to the one set in the SEO block. Also, some <meta> tags should appear in the <head> section. Check it:

    ![SEO data applied](media/seo-data-applied.png.png)



## Frontend - URL slugs (semantic URLs)

In this section, you'll configure semantic URLs and slug resolution to replace ID-based routing with SEO-friendly URLs.

1. Replace ID-based URLs with semantic ones:

    ```vue
    <router-link :to="articleRoute">
        <div class="text-left">{{ newsArticle.title }}</div>
    </router-link>
        
    <script lang="ts" setup>      
    const articleRoute = computed(() => {
      if (newsArticle.value?.seoInfo?.semanticUrl) {
        return {
          path: `/news/${newsArticle.value?.seoInfo?.semanticUrl}`,
        };
      }

    //ID-based link in case no seoInfo was found
      return {
        name: "NewsArticle",
        params: { articleId: newsArticle.value?.id },
      };
    });
    </script>
    ```

1. If you are using an URL not matching to any route (like **https://localhost:3000/heat-in-france**), you have to modify the **slug-content.vue** page to handle your object type.

    ```vue
    <template>
    <div v-if="isVisible && !loading && (hasContent || objectType || hasPageDocumentContent)" class="slug-content">
        <!--Other object type pages omitted-->
        <NewsArticlePage v-else-if="objectType === ObjectType.NewsArticle"
          :article-id="slugInfo?.entityInfo?.objectId ?? ''" />
    </div>
    </template>  

    <script setup lang="ts">
    //Not relevant code omitted
    const NewsArticlePage = defineAsyncComponent(() => import("@/modules/news/pages/news-article.vue"));

    enum ObjectType {
    //Other object types omitted
    NewsArticle = "NewsArticle",//The same value is in SeoInfoEntity class (hopefully you noted it in "Backend (database and UI)" code examples) 
    }

    watchEffect(() => {
    if (loading.value) {
        emit("setState", "loading");
    } else if (
        //Add your ObjectType here
        [ObjectType.Catalog, ObjectType.Category, ObjectType.CatalogProduct, ObjectType.Brands, ObjectType.Brand, ObjectType.NewsArticle].includes(
        objectType.value as ObjectType,
        )
    ) {
        emit("setState", "ready");
    } else if (pageDocumentContent.value) {
        emit("setState", "ready");
    } else if (pageContent.value) {
        emit("setState", "ready");
    } else {
        emit("setState", "empty");
    }
    });

    watch(slugInfo, () => {
    const type = slugInfo.value?.entityInfo?.objectType;
    switch (type) {
        //Other object types omitted
        case ObjectType.NewsArticle:
        setMatchingRouteName("NewsArticle");
        break;  
    }
    });
    </script>
    ```

1. Register **SeoResolver** - a Service that can map semantic URLs to object types and IDs. It’s recommended to use all URL segments for SEO data resolving (to avoid false-positive matches with URLs like **https://localhost:3000/foo-bar-75wrwnsneq/heat-in-france**):

    1. 
        ```csharp
        public interface INewsArticleSeoResolver : ISeoResolver
        {
            public Task<IList<SeoInfo>> FindActiveSeoAsync(string[] linkSegments, string storeId, string languageCode);
        }
        ```

    1. 
        ```csharp
        public class NewsArticleSeoResolver(Func<INewsArticleRepository> repositoryFactory) : INewsArticleSeoResolver
        {
            protected const string allowedUrlFirstSegment = "news";

            public async Task<IList<SeoInfo>> FindSeoAsync(SeoSearchCriteria criteria)
            {
                var linkSegments = GetLinkSegments(criteria);

                if (!LinkIsValid(linkSegments))
                {
                    return [];
                }

                return await FindActiveSeoAsync(linkSegments, criteria.StoreId, criteria.LanguageCode);
            }

            public virtual async Task<IList<SeoInfo>> FindActiveSeoAsync(string[] linkSegments, string storeId, string languageCode)
            {
                var lastLinkSegment = linkSegments.Last();

                using var repository = repositoryFactory();

                var seoInfoQuery = repository.NewsArticleSeoInfos.Where(x => x.IsActive && x.Keyword == lastLinkSegment);

                if (!storeId.IsNullOrEmpty())
                {
                    seoInfoQuery = seoInfoQuery.Where(x => x.StoreId == storeId);
                }

                if (!languageCode.IsNullOrEmpty())
                {
                    seoInfoQuery = seoInfoQuery.Where(x => x.LanguageCode == languageCode);
                }

                var seoEntities = await seoInfoQuery.ToListAsync();

                return seoEntities
                    .Select(x => x.ToModel(AbstractTypeFactory<SeoInfo>.TryCreateInstance()))
                    .ToList();
            }

            protected virtual string[] GetLinkSegments(SeoSearchCriteria criteria)
            {
                var link = criteria?.Permalink ?? criteria?.Slug;

                if (link.IsNullOrEmpty())
                {
                    return [];
                }

                return link.Split('/', StringSplitOptions.RemoveEmptyEntries);
            }

            protected virtual bool LinkIsValid(string[] linkSegments)
            {
                if ((linkSegments.Length == 0) || (linkSegments.Length > 2) || (linkSegments.Length == 2 && !linkSegments[0].EqualsIgnoreCase(allowedUrlFirstSegment)))
                {
                    return false;
                }

                return true;
            }
        }
        ```

1. If you are using an URL segment (**news/** in the code above will produce **https://localhost:3000/news/heat-in-france** link) matching an an existing route, the semantic URL should be resolved in your entity page. One option is just treat it as an alternative ID and handle it in the xAPI:

    ```csharp
        public async Task<NewsArticle> Handle(NewsArticleQuery request, CancellationToken cancellationToken)
        {
            var result = await newsArticleService.GetNoCloneAsync(request.Id);

            //This block was added to handle semantic URLs
            if (result == null)
            {
                var newsArticleSeoInfo = await newsArticleSeoResolver.FindActiveSeoAsync([request.Id], request.StoreId, request.LanguageCode);
                if (!newsArticleSeoInfo.IsNullOrEmpty())
                {
                    result = await newsArticleService.GetNoCloneAsync(newsArticleSeoInfo.First().ObjectId);
                }
            }

            if (result != null)
            {
                await PostProcessResultAsync(request.StoreId, request.LanguageCode, [result]);
            }

            return result;
        }
    ```


Now you should be able to reach your object page with a URL slug (as long as you have the SEO data for that particular object):

![Final result](media/final-result.png)


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../overview">← SEO feature overview </a>
    <a href="../configuration">Configuration →</a>
</div>
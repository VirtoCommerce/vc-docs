# newsArticles ==~query~==

This query allows you to retrieve a list of news articles published on the Frontend.

## Arguments

| Argument                   | Description                                                                               |
| -------------------------- | ----------------------------------------------------------------------------------------- |
| `after` ==String==         | Returns articles after the specified cursor (used for pagination).                        |
| `first` ==Int==            | The maximum number of articles to return, starting after the cursor specified by `after`. |
| `keyword` ==String==       | A keyword to search for within news articles.                                             |
| `sort` ==String==          | Sorting parameter (for example, by publish date or title).                                |
| `storeId` ==String!==      | The ID of the store where the news articles are published.                                |
| `languageCode` ==String!== | The language code to retrieve the articles in.                                            |
| `userId` ==String==        | The ID of the user, used if filtering articles per user is needed.                        |

## Possible returns

| Possible return                                                                 | Description                                                       |
| ------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| [`NewsArticleContentConnection`](../objects/NewsArticleContentConnection.md)    | A paginated collection of news articles and their related fields. |

## Example

<div class="grid" markdown>

```json title="Query"
{
newsArticles(
    storeId: "B2B-store"
    languageCode: "en-US"
) {
    items {
      id
      title
      content
      contentPreview
      publishDate
      seoInfo {
        id
        name
        semanticUrl
        pageTitle
        metaDescription
        metaKeywords
      }
    }
  }
}
```

```json title="Return"
{
  "data": {
    "newsArticles": {
      "items": [
        {
          "id": "4ae1bb12-fd8f-4dcf-be92-9d5ad50b2a62",
          "title": "First News Article",
          "content": "<p>This is the full content of the first article.</p>",
          "contentPreview": "This is the preview of the first article...",
          "publishDate": "2025-08-19T10:30:00Z",
          "seoInfo": {
            "id": "seo-123",
            "name": "first-news-article",
            "semanticUrl": "first-news-article",
            "pageTitle": "First News Article",
            "metaDescription": "A short description of the first article.",
            "metaKeywords": "news, update, commerce"
          }
        },
        {
          "id": "7bf9ce21-d02b-4dbb-b91a-7aebc7c7aaf3",
          "title": "Second News Article",
          "content": "<p>This is the full content of the second article.</p>",
          "contentPreview": "This is the preview of the second article...",
          "publishDate": "2025-08-18T15:00:00Z",
          "seoInfo": {
            "id": "seo-124",
            "name": "second-news-article",
            "semanticUrl": "second-news-article",
            "pageTitle": "Second News Article",
            "metaDescription": "A short description of the second article.",
            "metaKeywords": "announcement, commerce"
          }
        }
      ]
    }
  }
}
```

</div>
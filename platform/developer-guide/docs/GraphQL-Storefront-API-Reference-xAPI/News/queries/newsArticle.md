# newsArticle ==~query~==

This query allows you to retrieve a specific news article published on the Frontend.

## Arguments

| Argument                   | Description                                                   |
| -------------------------- | ------------------------------------------------------------- |
| `id` ==String!==           | The unique identifier of the news article.                    |
| `storeId` ==String!==      | The ID of the store where the news article is published.      |
| `languageCode` ==String!== | The language code to retrieve the article in.                 |

## Possible returns

| Possible return                                            | Description                                                       |
| ---------------------------------------------------------- | ----------------------------------------------------------------- |
| [`NewsArticleContent`](../objects/NewsArticleContent.md) | Defines the fields and properties associated with a news article. |

## Example

<div class="grid" markdown>

```json title="Query"
{
  newsArticle(
    id: "4ae1bb12-fd8f-4dcf-be92-9d5ad50b2a62"
    storeId: "B2B-store"
    languageCode: "en-US"
  ) {
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
```

```json title="Return"
{
  "data": {
    "newsArticle": {
      "id": "4ae1bb12-fd8f-4dcf-be92-9d5ad50b2a62",
      "title": "Sample News Title",
      "content": "<p>This is the full content of the news article.</p>",
      "contentPreview": "This is the preview of the article...",
      "publishDate": "2025-08-19T10:30:00Z",
      "seoInfo": {
        "id": "8ff3f8b4-b8c3-42ad-9a3e-92e6b5a0c4e0",
        "name": "sample-news-title",
        "semanticUrl": "sample-news-title",
        "pageTitle": "Sample News Title",
        "metaDescription": "A short description for SEO purposes.",
        "metaKeywords": "news, commerce, update"
      }
    }
  }
}
```

</div>
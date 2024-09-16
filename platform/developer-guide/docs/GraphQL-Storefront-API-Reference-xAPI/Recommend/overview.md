# xRecommend

The xRecommend module adds an extensible query to Virto Commerce Platform that allows you to display recommendations. 

The xRecommend module adds the XAPI product recommendation query to the Virto Commerce Platform GraphQL schema. The API provides a list of recommended products based on semantic similarities in product names and other searchable properties. The module is designed to be plug and play, seamlessly integrating with backend and frontend to enhance the user experience by providing intelligent product recommendations.

| Queries                                                                                     | Objects                                                                     | Mutations                     |
|---------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|-------------------------------|
| [recommendations](query/recommendations.md)<br> [recentlyBrowsed](query/recentlyBrowsed.md) | [GetRecommendationsResponseType](object/GetRecommendationsResponseType.md)  <br> [GetRecentlyBrowsedResponseType](object/GetRecentlyBrowsedResponseType.md) <br> [InputPushHistoricalEventType](object/InputPushHistoricalEventType.md)| [pushHistoricalEvent](mutation/pushHistoricalEvent.md) |

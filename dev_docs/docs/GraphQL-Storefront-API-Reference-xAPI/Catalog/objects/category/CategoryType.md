# CategoryType ==~object~==

`CategoryType` is used to differentiate or group different types of categories.

<style type="text/css">
.tg  {border:none;border-collapse:collapse;border-spacing:0;}
.tg td{border-color:white;border-style:solid;border-width:1px;font-family:Circular Std;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:white;border-style:solid;border-width:1px;font-family:Circular Std;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-0lax{border-color:#ffffff;text-align:left;vertical-align:top}
.tg .tg-0pky:nth-child(1),
.tg .tg-0lax:nth-child(1) {width: 25%;}
.tg .tg-0pky:nth-child(2),
.tg .tg-0lax:nth-child(2) {width: 75%;}
</style>
<table class="tg">
<tbody>
<tr>
    <td class="tg-0pky"><code>id</code> {==String!==}</td>
    <td class="tg-0pky">The Id of the category.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>imgSrc</code> {==String==}</td>
    <td class="tg-0pky">The category image.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>code</code> {==String!==}</td>
    <td class="tg-0pky">The SKU of the category.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>name</code> {==String!==}</td>
    <td class="tg-0pky">The name of the category.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>level</code> {==Int==}</td>
    <td class="tg-0pky">Level in the hierarchy.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>priority</code> {==Int!==}</td>
    <td class="tg-0pky">The priority of the category in relation to other categories.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>outline</code> {==String==}</td>
    <td class="tg-0pky">The hierarchical outline of the category.</td>
</tr>
<tr>
    <td class="tg-0pky"><code>slug</code> {==String==}</td>
    <td class="tg-0pky">The URL slug of the category.</td>
</tr>
<tr>
    <td class="tg-sxqf"><code>path</code> {==String==}</td>
    <td class="tg-0pky">The full path of the category within the category hierarchy.</td>
</tr>
<tr>
    <td class="tg-0lax"><code>seoInfo</code> {==<a href="../../SeoInfo">SeoInfo</a>==}</td>
    <td class="tg-0lax">Request related SEO info.</td>
</tr>
<tr>
    <td class="tg-0lax"><code>descriptions(...)</code> {==<a href="../CategoryDescriptionType">CategoryDescriptionType</a>==}</td>
    <td class="tg-0lax"> Additional descriptions for the category in different languages.</td>
</tr>
<tr>
    <td class="tg-0lax"><code>description(...)</code> {==<a href="../CategoryDescriptionType">CategoryDescriptionType</a>==}</td>
    <td class="tg-0lax">The description of the category in a specific language.</td>
</tr>
<tr>
    <td class="tg-0lax"><code>parent</code> {==Category==}</td>
    <td class="tg-0lax">The parent category of the current category.</td>
</tr>
<tr>
    <td class="tg-0lax"><code>hasParent</code> {==Boolean==}</td>
    <td class="tg-0lax">Indicates whether the category has a parent category.</td>
</tr>
<tr>
    <td class="tg-0lax"><code>outlines</code> {==<a href="../../OutlineType/OutlineType">OutlineType</a>==}</td>
    <td class="tg-0lax">The hierarchical outlines of the category and its ancestors.</td>
</tr>
<tr>
    <td class="tg-0lax"><code>images</code> {==<a href="../../ImageType">ImageType</a>==}</td>
    <td class="tg-0lax">The images associated with the category.</td>
</tr>
<tr>
    <td class="tg-0lax"><code>breadcrumbs</code> {==<a href="../../Breadcrumb">Breadcrumb</a>==}</td>
    <td class="tg-0lax">The breadcrumbs representing the category's position in the category hierarchy.</td>
</tr>
<tr>
    <td class="tg-0lax"><code>properties(...)</code> {==<a href="../../Property/Property">Property</a>==}</td>
    <td class="tg-0lax">The properties associated with the category.</td>
</tr>
<tr>
    <td class="tg-0lax"><code>childCategories</code> {==Category==}</td>
    <td class="tg-0lax">The child categories of the current category.</td>
</tr>
</tbody>
</table>

[Read more about managing categories](https://docs.virtocommerce.org/new/user_docs/catalog/managing-categories/){ .md-button }

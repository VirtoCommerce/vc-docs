# Child Categories 

This query allows you to retrieve a list of child categories for a given parent category. You can also retrieve their names, ids, and urls. This information can be used to build custom user interfaces or to retrieve data for other purposes within your application.

## Example
```
query {
    childCategories(
        storeId: "test"
        categoryId: null
        maxLevel: 2
        onlyActive: true
    ) {
        childCategories {
            name
            childCategories {
                name
            }
        }
    }
}
```
## Result 

![Request Child Categories](../../media/request-child-categories.png)



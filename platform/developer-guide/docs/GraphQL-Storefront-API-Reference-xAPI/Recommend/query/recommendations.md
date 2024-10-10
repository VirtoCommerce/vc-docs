# Recommendations ==~query~==

This query allows you to retrieve product recommendations based on various criteria.

## Arguments

| Argument                       | Description                                                                                     |
|--------------------------------|-------------------------------------------------------------------------------------------------|
| `storeId` ==String!==          | The ID of the store to retrieve recommendations from.                                           |
| `userId`  ==String==           | The ID of the user.                                                                             |
| `cultureName` ==String==       | The language to retrieve data in.                                                               |
| `currencyCode` ==String!==     | A standardized code for the specific currency.                                                  |
| `productId` ==String==         | The ID of the product for which recommendations are requested.                                  |
| `model` ==String==             | The recommendation model to use (e.g., **related-products** or **bought-together**).            |
| `fallbackProductsFilter` ==String== | A filter to apply when no recommendations are found.                                       |
| `maxRecommendations` ==String== | The maximum number of recommendations to return.                                               |

## Possible return

| Possible return                                         	| Description                                                              	|
|---------------------------------------------------------	|------------------------------------------------------------------------	|
| [`GetRecommendationsResponseType`](../object/GetRecommendationsResponseType.md)  | Defines the properties and fields associated with the recommendations response. 	|

## Examples

=== "Related products query"
    ```json linenums="1"
    {
      recommendations(
        storeId: "Electronics"
        cultureName: "en-US"
        model: "related-products"
        productId: "Product-ID-12345"
        currencyCode: "USD"
        maxRecommendations: 5
      ) {
        products {
          id
          name
          code  
        }
      }
    }
    ```

=== "Return"
    ```json linenums="1"
    {
      "data": {
        "recommendations": {
          "products": [
            {
              "id": "product-1",
              "name": "Smartphone XYZ",
              "code": "XYZ123"
            },
            {
              "id": "product-2",
              "name": "Smartphone ABC",
              "code": "ABC456"
            }
          ]
        }
      }
    }
    ```

=== "Products bought together query "
    ```json linenums="1"
    query GetProductRecommendations(
      $storeId: String!
      $userId: String
      $currencyCode: String
      $cultureName: String
      $productId: String
      $model: String
      $maxRecommendations: Int
    ) {
      recommendations(
        storeId: "B2B-store"
        userId: "bd502614-9e68-4920-a4ac-3f51e258d8d2"
        productId: "7d93937c-740b-420c-9a34-3353dc0aaa22"
        currencyCode: "USD"
        cultureName: "en-US
        model: "bought-together"
        maxRecommendations: 6
      ) {
        products {
          id
          name
          code
          hasVariations
          imgSrc
          vendor {
            name
          }
          price {
            actual {
              amount
              formattedAmount
            }
            list {
              amount
              formattedAmount
            }
          }
          minVariationPrice {
            actual {
              amount
              formattedAmount
            }
            list {
              amount
              formattedAmount
            }
          }
        }
      }
    }
    ```

=== "Return"
    ```json linenums="1"
    {
        "data": {
            "recommendations": {
                "products": [
                    {
                        "id": "2a7412c0-fa88-4c98-b2ef-1a7312d68f7b",
                        "name": "3D Kawaii Pencil Case Girls Decompression Pen Pouch Cute Waterproof School Supplies Aesthetic Organizer Box  Korean Stationery",
                        "code": "ALCOE2126",
                        "hasVariations": false,
                        "imgSrc": "https://ae01.alicdn.com/kf/S72aa2e07a98c4cb59c057ffae5657838p/3D-Kawaii-Pencil-Case-Girls-Decompression-Pen-Pouch-Cute-Waterproof-School-Supplies-Aesthetic-Organizer-Box-Korean.jpg_470x470.jpg_.webp",
                        "vendor": null,
                        "price": {
                            "actual": {
                                "amount": 99.990,
                                "formattedAmount": "$99.99"
                            },
                            "list": {
                                "amount": 100.000,
                                "formattedAmount": "$100.00"
                            }
                        },
                        "minVariationPrice": {
                            "actual": {
                                "amount": 99.99,
                                "formattedAmount": "$99.99"
                            },
                            "list": {
                                "amount": 99.99,
                                "formattedAmount": "$99.99"
                            }
                        }
                    },
                    {
                        "id": "46415f23-f4dd-4a77-916f-f1ba2ebceac4",
                        "name": "Soft Wavy Lines Phone Case For iphone 15 11 12 13 14 Pro Max XS MaxCandy Bumper Transparent Cases Cover",
                        "code": "PA583787",
                        "hasVariations": false,
                        "imgSrc": "https://ae01.alicdn.com/kf/S9a0635405cd0491583b73797eda9c5fdU/Soft-Wavy-Lines-Phone-Case-For-iphone-15-11-12-13-14-Pro-Max-XS-MaxCandy.jpg_470x470.jpg_.webp",
                        "vendor": null,
                        "price": {
                            "actual": {
                                "amount": 99.990,
                                "formattedAmount": "$99.99"
                            },
                            "list": {
                                "amount": 100.000,
                                "formattedAmount": "$100.00"
                            }
                        },
                        "minVariationPrice": {
                            "actual": {
                                "amount": 99.99,
                                "formattedAmount": "$99.99"
                            },
                            "list": {
                                "amount": 99.99,
                                "formattedAmount": "$99.99"
                            }
                        }
                    },
                    {
                        "id": "ef011d8b-7cae-46cf-86b3-e62334c08c3a",
                        "name": "3pcs/lot Cartoon Creative Fruit Eraser Pupils Exam Pencil Eraser Children's Stationery Painting Sketch Eraser  School  Kawaii",
                        "code": "ALCOE6380",
                        "hasVariations": false,
                        "imgSrc": "https://ae01.alicdn.com/kf/Sc39b47a7cdc24b818eefd4219456e231u/3pcs-lot-Cartoon-Creative-Fruit-Eraser-Pupils-Exam-Pencil-Eraser-Children-s-Stationery-Painting-Sketch-Eraser.jpg_470x470.jpg_.webp",
                        "vendor": null,
                        "price": {
                            "actual": {
                                "amount": 99.990,
                                "formattedAmount": "$99.99"
                            },
                            "list": {
                                "amount": 100.000,
                                "formattedAmount": "$100.00"
                            }
                        },
                        "minVariationPrice": {
                            "actual": {
                                "amount": 99.99,
                                "formattedAmount": "$99.99"
                            },
                            "list": {
                                "amount": 99.99,
                                "formattedAmount": "$99.99"
                            }
                        }
                    },
                    {
                        "id": "f33bae48-c89f-477b-972c-1986405beb45",
                        "name": "14 K Rhodium Plated Rose Gold Ring  - fineness 14 K",
                        "code": "LJE-78218335",
                        "hasVariations": false,
                        "imgSrc": "https://s1.apart.pl/products/jewellery/packshot/73065/apart-189-353--0.jpg",
                        "vendor": null,
                        "price": {
                            "actual": {
                                "amount": 123.000,
                                "formattedAmount": "$123.00"
                            },
                            "list": {
                                "amount": 123.000,
                                "formattedAmount": "$123.00"
                            }
                        },
                        "minVariationPrice": {
                            "actual": {
                                "amount": 123.0,
                                "formattedAmount": "$123.00"
                            },
                            "list": {
                                "amount": 123.0,
                                "formattedAmount": "$123.00"
                            }
                        }
                    },
                    {
                        "id": "e3689aabceb44a12be512ec0acd89887",
                        "name": "Epson Expression Premium XP-820 Wireless Color Photo Printer/Copier/Scanner/Fax Machine",
                        "code": "553390824",
                        "hasVariations": false,
                        "imgSrc": "https://vcst-qa.govirto.com/cms-content/assets/catalog/5aa50/553390824/epson-xp820-1.jpg",
                        "vendor": null,
                        "price": {
                            "actual": {
                                "amount": 1000.000,
                                "formattedAmount": "$1,000.00"
                            },
                            "list": {
                                "amount": 1200.000,
                                "formattedAmount": "$1,200.00"
                            }
                        },
                        "minVariationPrice": {
                            "actual": {
                                "amount": 1000.0,
                                "formattedAmount": "$1,000.00"
                            },
                            "list": {
                                "amount": 1000.0,
                                "formattedAmount": "$1,000.00"
                            }
                        }
                    },
                    {
                        "id": "98bbbdcc-c4ef-4ca3-85b5-4c14da3ab85a",
                        "name": "5pcs Kawaii Sanrio Gel Pen Kuromi Melody Hello Kitty Cinnamoroll Pressing Gel Pen for Girls Students School Supplies Stationery",
                        "code": "ALCOE3475",
                        "hasVariations": false,
                        "imgSrc": "https://ae01.alicdn.com/kf/Sb2882c275c48475f9d77151a4579317b6/5pcs-Kawaii-Sanrio-Gel-Pen-Kuromi-Melody-Hello-Kitty-Cinnamoroll-Pressing-Gel-Pen-for-Girls-Students.jpg_470x470.jpg_.webp",
                        "vendor": null,
                        "price": {
                            "actual": {
                                "amount": 99.990,
                                "formattedAmount": "$99.99"
                            },
                            "list": {
                                "amount": 100.000,
                                "formattedAmount": "$100.00"
                            }
                        },
                        "minVariationPrice": {
                            "actual": {
                                "amount": 99.99,
                                "formattedAmount": "$99.99"
                            },
                            "list": {
                                "amount": 99.99,
                                "formattedAmount": "$99.99"
                            }
                        }
                    }
                ]
            }
        }
    }
    ```

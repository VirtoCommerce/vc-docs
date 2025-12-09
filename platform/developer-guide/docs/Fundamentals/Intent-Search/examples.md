# Examples

The Intent Search system supports 17 different intent classes and can intelligently combine them for comprehensive query analysis.

## Exact product identification

**ExactId & StandardCode Classes**

```json
// Input: "SKU-12345-ABC"
{
  "searchText": "SKU-12345-ABC",
  "response": {
    "tokenAnalysis": [
      {
        "token": "SKU-12345-ABC",
        "detectedClass": "ExactId",
        "matchedValue": "SKU-12345-ABC",
        "category": "SKU",
        "confidence": 1.0
      }
    ],
    "refinedQuery": ""
  }
}

// Other exact ID examples:
"UPC-123456789012"       → UPC code
"EAN-1234567890123"      → EAN barcode
"ASIN-B08N5WRWNW"        → Amazon identifier
"MPN-ABC123XYZ"          → Manufacturer part number
```

## Brand and model recognition

**BrandModel сlass**

```json
// Input: "iPhone 14 Pro Max"
{
  "searchText": "iPhone 14 Pro Max",
  "response": {
    "tokenAnalysis": [
      {
        "token": "iPhone 14 Pro Max",
        "detectedClass": "BrandModel",
        "matchedValue": "Apple iPhone 14 Pro Max",
        "category": "Mobile Phone",
        "confidence": 0.98
      }
    ],
    "facets": {
      "Brand": {
        "facetName": "Brand",
        "values": ["Apple"],
        "confidence": 0.98,
        "matchedTokens": ["iPhone"]
      }
    }
  }
}

// Other brand/model examples:
"Samsung Galaxy S23"     → Brand: Samsung, Model: Galaxy S23
"MacBook Air M2"         → Brand: Apple, Model: MacBook Air M2
"Tesla Model Y"          → Brand: Tesla, Model: Model Y
```

## Technical specifications

**TechnicalSpec & Dimension Classes**

```json
// Input: "2.5 inch LCD display 5V 2A"
{
  "searchText": "2.5 inch LCD display 5V 2A",
  "response": {
    "tokenAnalysis": [
      {
        "token": "2.5 inch",
        "detectedClass": "TechnicalSpec",
        "matchedValue": "2.5 inch",
        "category": "Length",
        "standardizedValue": "2.5 in",
        "confidence": 0.95
      },
      {
        "token": "5V",
        "detectedClass": "TechnicalSpec",
        "matchedValue": "5V",
        "category": "Voltage",
        "standardizedValue": "5 V",
        "confidence": 0.92
      },
      {
        "token": "2A",
        "detectedClass": "TechnicalSpec",
        "matchedValue": "2A",
        "category": "Current",
        "standardizedValue": "2 A",
        "confidence": 0.90
      }
    ],
    "facets": {
      "DisplaySize": {
        "facetName": "DisplaySize",
        "values": ["2.5\""],
        "confidence": 0.95,
        "matchedTokens": ["2.5 inch"]
      }
    }
  }
}

// Other technical spec examples:
"32GB storage capacity"  → "32 GB"
"100MHz processor"       → "100 MHz"
"12V DC motor"          → "12 V"
```

## Product features and attributes

**Feature Class**

```json
// Input: "red leather waterproof case"
{
  "searchText": "red leather waterproof case",
  "response": {
    "tokenAnalysis": [
      {
        "token": "red",
        "detectedClass": "Feature",
        "matchedValue": "Red",
        "category": "Color",
        "confidence": 0.95
      },
      {
        "token": "leather",
        "detectedClass": "Feature",
        "matchedValue": "Leather",
        "category": "Material",
        "confidence": 0.90
      },
      {
        "token": "waterproof",
        "detectedClass": "Feature",
        "matchedValue": "Waterproof",
        "category": "Protection",
        "confidence": 0.88
      }
    ],
    "facets": {
      "Color": {
        "facetName": "Color",
        "values": ["Red"],
        "confidence": 0.95,
        "matchedTokens": ["red"]
      },
      "Material": {
        "facetName": "Material",
        "values": ["Leather"],
        "confidence": 0.90,
        "matchedTokens": ["leather"]
      }
    }
  }
}
```

## Product categories

**ProductType Class**

```json
// Input: "gaming laptop"
{
  "searchText": "gaming laptop",
  "response": {
    "categories": [
      {
        "categoryId": "electronics-computers-laptops-gaming",
        "categoryName": "Electronics > Computers > Laptops > Gaming Laptops",
        "score": 0.88
      }
    ],
    "tokenAnalysis": [
      {
        "token": "gaming laptop",
        "detectedClass": "ProductType",
        "matchedValue": "Gaming Laptop",
        "category": "Electronics",
        "confidence": 0.88
      }
    ]
  }
}

// Other category examples:
"running shoes"          → Sports & Outdoors > Athletic Shoes > Running
"kitchen blender"        → Home & Kitchen > Small Appliances > Blenders
"winter coat"            → Clothing > Outerwear > Coats & Jackets
```

## Price and budget
**Price Class**

```json
// Input: "bluetooth headphones under $100"
{
  "searchText": "bluetooth headphones under $100",
  "response": {
    "tokenAnalysis": [
      {
        "token": "under $100",
        "detectedClass": "Price",
        "matchedValue": "< $100",
        "category": "Budget",
        "confidence": 0.92
      },
      {
        "token": "bluetooth",
        "detectedClass": "Feature",
        "matchedValue": "Bluetooth",
        "category": "Connectivity",
        "confidence": 0.95
      }
    ],
    "facets": {
      "MaxPrice": {
        "facetName": "MaxPrice",
        "values": ["100"],
        "confidence": 0.92,
        "matchedTokens": ["under $100"]
      }
    }
  }
}
```

## Problem solving queries

**SymptomJob Class**

```json
// Input: "fix leaky faucet"
{
  "searchText": "fix leaky faucet",
  "response": {
    "tokenAnalysis": [
      {
        "token": "fix leaky faucet",
        "detectedClass": "SymptomJob",
        "matchedValue": "Plumbing Repair",
        "category": "Home Maintenance",
        "confidence": 0.85
      }
    ],
    "suggestedQueries": [
      "faucet repair kit",
      "plumbing tools",
      "faucet parts"
    ]
  }
}

// Other symptom/job examples:
"remove stains from carpet"    → Cleaning problem
"improve wifi signal"         → Network connectivity issue
"reduce noise in room"        → Acoustic problem
```

## Use case & application
**UseCase Class**

```json
// Input: "outdoor photography gear"
{
  "searchText": "outdoor photography gear",
  "response": {
    "tokenAnalysis": [
      {
        "token": "outdoor photography",
        "detectedClass": "UseCase",
        "matchedValue": "Outdoor Photography",
        "category": "Photography",
        "confidence": 0.82
      }
    ],
    "categories": [
      {
        "categoryId": "electronics-cameras-accessories",
        "categoryName": "Electronics > Cameras & Photo > Accessories",
        "score": 0.78
      }
    ]
  }
}

// Other use case examples:
"home office setup"          → Remote work environment
"camping equipment"          → Outdoor recreation
"baby safety products"       → Child safety
```

## Complex multi-intent queries

**Combined Intent Classes**

```json
// Input: "Samsung 55 inch 4K OLED TV under $2000"
{
  "searchText": "Samsung 55 inch 4K OLED TV under $2000",
  "response": {
    "tokenAnalysis": [
      {
        "token": "Samsung",
        "detectedClass": "BrandModel",
        "matchedValue": "Samsung",
        "category": "Brand",
        "confidence": 0.98
      },
      {
        "token": "55 inch",
        "detectedClass": "TechnicalSpec",
        "matchedValue": "55 inch",
        "category": "Screen Size",
        "standardizedValue": "55 in",
        "confidence": 0.95
      },
      {
        "token": "4K",
        "detectedClass": "TechnicalSpec",
        "matchedValue": "4K",
        "category": "Resolution",
        "standardizedValue": "4K Ultra HD",
        "confidence": 0.93
      },
      {
        "token": "OLED",
        "detectedClass": "Feature",
        "matchedValue": "OLED",
        "category": "Display Technology",
        "confidence": 0.90
      },
      {
        "token": "under $2000",
        "detectedClass": "Price",
        "matchedValue": "< $2000",
        "category": "Budget",
        "confidence": 0.92
      },
      {
        "token": "TV",
        "detectedClass": "ProductType",
        "matchedValue": "Television",
        "category": "Electronics",
        "confidence": 0.88
      }
    ],
    "facets": {
      "Brand": {
        "facetName": "Brand",
        "values": ["Samsung"],
        "confidence": 0.98,
        "matchedTokens": ["Samsung"]
      },
      "ScreenSize": {
        "facetName": "ScreenSize",
        "values": ["55\""],
        "confidence": 0.95,
        "matchedTokens": ["55 inch"]
      },
      "DisplayTechnology": {
        "facetName": "DisplayTechnology",
        "values": ["OLED"],
        "confidence": 0.90,
        "matchedTokens": ["OLED"]
      },
      "MaxPrice": {
        "facetName": "MaxPrice",
        "values": ["2000"],
        "confidence": 0.92,
        "matchedTokens": ["under $2000"]
      }
    },
    "categories": [
      {
        "categoryId": "electronics-tv-displays",
        "categoryName": "Electronics > TV & Video > Televisions",
        "score": 0.88
      }
    ],
    "refinedQuery": "",
    "performance": {
      "totalProcessingTime": "145ms",
      "classifierBreakdown": {
        "BrandModel": "23ms",
        "TechnicalSpec": "34ms",
        "Feature": "28ms",
        "Price": "31ms",
        "ProductType": "29ms"
      }
    }
  }
}
```

## Non-product queries

**NonProduct Class**

```json
// Input: "how to install the software"
{
  "searchText": "how to install the software",
  "response": {
    "tokenAnalysis": [
      {
        "token": "how to install the software",
        "detectedClass": "NonProduct",
        "matchedValue": "Support Question",
        "category": "Installation Help",
        "confidence": 0.90
      }
    ],
    "suggestedQueries": [
      "installation guide",
      "setup instructions",
      "technical support"
    ]
  }
}

// Other non-product examples:
"store hours"               → Business information
"shipping policy"           → Service information
"contact customer service"  → Support request
"track my order"           → Order status inquiry
```



<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../installation-and-configuration">← Installation and configuration</a>
    <a href="../../Persistence/DB-Agnostic/overview">DB agnostic architecture  overview→</a>
</div>

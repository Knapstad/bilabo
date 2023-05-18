import requests

headers = {
    "authority": "www.volvocars.com",
    "accept": "*/*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,nb;q=0.7,no;q=0.6,sv;q=0.5",
    "apollographql-client-name": "car-selector",
    "content-type": "application/json",
    "origin": "https://www.volvocars.com",
    "referer": "https://www.volvocars.com/no/shop/?filters.availability=inStock",
    "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    #'traceparent': '00-0a9fd6c11bd75cc67db1651e3d296b0b-2533031146b89169-01',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
}

json_data = {
    "operationName": "StockCarsQuery",
    "variables": {
        "CLEFilter": {
            "excludeDuplicates": True,
            "take": 100,
            "filter": {
                "value": {
                    "marketCode": {
                        "value": {
                            "value": "NO",
                        },
                    },
                },
            },
        },
        "locale": "no-NO",
        "customerType": "b2c",
        "taxation": [
            {
                "carType": "",
                "modelYear": "",
                "date": "",
            },
            {
                "carType": "",
                "modelYear": "",
                "date": "",
            },
            {
                "carType": "",
                "modelYear": "",
                "date": "",
            },
            {
                "carType": "",
                "modelYear": "",
                "date": "",
            },
            {
                "carType": "",
                "modelYear": "",
                "date": "",
            },
        ],
        "mileage": None,
        "isFixedOnly": True,
        "contractLength": None,
        "downpayment": None,
        "companyCarMileage": "1",
        "skipCashPricesForStock": True,
    },
    "query": 'query StockCarsQuery($CLEFilter: CLESearchFilter!, $locale: String!, $customerType: String!, $priceDates: [TaxationInput!], $taxation: [TaxationInput!], $isFixedOnly: Boolean!, $skipCashPricesForStock: Boolean!, $mileage: Float, $contractLength: Float, $downpayment: Float, $companyCarMileage: String!) {\n  stockSubscriptionCars(filter: $CLEFilter) {\n    hits {\n      vehicle {\n        id\n        duplicatesIdentifier\n        availability {\n          available\n          __typename\n        }\n        market {\n          marketCode\n          __typename\n        }\n        order {\n          estimatedCustomerDeliveryLeadTime\n          estimatedCustomerDeliveryLeadTimeUnit\n          __typename\n        }\n        configuration {\n          options {\n            code\n            description {\n              text\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        specification {\n          ...CLP_SHARED_FIELDS\n          ...PRICE_SUMMARY_SHARED_FIELDS_STOCK\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment CLP_SHARED_FIELDS on Car {\n  ...GENERAL_SHARED_FIELDS\n  technicalData(locale: $locale) {\n    electricRangeWltpTotal {\n      formatted\n      __typename\n    }\n    fuelConsumptionWltpTotal {\n      formatted\n      __typename\n    }\n    horsepowerTotal {\n      exactValue {\n        formatted\n        __typename\n      }\n      __typename\n    }\n    kilowattsTotal {\n      exactValue {\n        formatted\n        __typename\n      }\n      __typename\n    }\n    cargoCapacity {\n      formatted\n      __typename\n    }\n    co2EmissionsWltpTotal {\n      formatted\n      __typename\n    }\n    __typename\n  }\n  options {\n    code\n    content(locale: $locale) {\n      displayName {\n        value\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  features {\n    code\n    globalName\n    globalShortName\n    content(locale: $locale) {\n      displayName {\n        value\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  visualizations(marketOrLocale: $locale) {\n    views {\n      interior {\n        studio {\n          seat {\n            sizes {\n              default {\n                url\n                __typename\n              }\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      exterior {\n        studio {\n          threeQuartersFrontLeft {\n            sizes {\n              default {\n                transparentUrl\n                __typename\n              }\n              __typename\n            }\n            __typename\n          }\n          front {\n            sizes {\n              default {\n                url\n                __typename\n              }\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment GENERAL_SHARED_FIELDS on Car {\n  btoDeliveryLeadTimeToMarket(locale: $locale) {\n    formatted\n    __typename\n  }\n  carKeyExpanded {\n    modelYear\n    __typename\n  }\n  carType {\n    content(locale: $locale) {\n      seatCapacity {\n        value\n        __typename\n      }\n      modelCode\n      carTypeCategory {\n        value\n        __typename\n      }\n      displayName {\n        value\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  color {\n    code\n    content(locale: $locale) {\n      displayName {\n        value\n        __typename\n      }\n      hex {\n        value\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  driveline {\n    content(locale: $locale) {\n      transmissionType {\n        value\n        __typename\n      }\n      driveType {\n        value\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  engine {\n    content(locale: $locale) {\n      fuelType {\n        formatted\n        value\n        __typename\n      }\n      engineType {\n        value\n        __typename\n      }\n      shortName {\n        value\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  model(locale: $locale) {\n    key\n    displayName {\n      value\n      __typename\n    }\n    __typename\n  }\n  modelFamily(locale: $locale) {\n    displayName {\n      value\n      __typename\n    }\n    __typename\n  }\n  pno {\n    pno12\n    pno34PlusOptions\n    __typename\n  }\n  trim(locale: $locale) {\n    displayName {\n      value\n      __typename\n    }\n    description {\n      value\n      __typename\n    }\n    __typename\n  }\n  upholstery {\n    code\n    content(locale: $locale) {\n      upholsteryMaterial {\n        formatted\n        __typename\n      }\n      displayName {\n        value\n        __typename\n      }\n      upholsteryCode\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment PRICE_SUMMARY_FIELDS on CarPriceSummary {\n  all {\n    subscriptionVatAmount {\n      amount\n      __typename\n    }\n    __typename\n  }\n  price {\n    amount\n    display\n    __typename\n  }\n  priceWithoutTax {\n    amount\n    __typename\n  }\n  taxes {\n    all {\n      vatPosition\n      vatRate\n      __typename\n    }\n    informational {\n      tags\n      price {\n        display\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  subscriptionPrices {\n    contractLength\n    __typename\n  }\n  __typename\n}\n\nfragment PRICE_SUMMARY_SHARED_FIELDS_STOCK on Car {\n  priceSummaryCash: priceSummary(\n    priceConfigInput: {locale: $locale, name: "cash", priceDates: $priceDates, roundingStrategy: alwaysRound, taxation: $taxation, variableReferences: [{name: "customerType", value: $customerType}, {name: "CompanyCarMileage", value: $companyCarMileage}]}\n  ) {\n    ...PRICE_SUMMARY_FIELDS @skip(if: $skipCashPricesForStock)\n    __typename\n  }\n  ...PRICE_SUMMARY_SUB\n  ...PRICE_SUMMARY_SUB_FIXED\n  __typename\n}\n\nfragment PRICE_SUMMARY_SUB on Car {\n  priceSummarySub: priceSummary(\n    priceConfigInput: {locale: $locale, name: "sub", priceDates: $priceDates, roundingStrategy: alwaysRound, taxation: $taxation, variableReferences: [{name: "customerType", value: $customerType}, {name: "CompanyCarMileage", value: $companyCarMileage}]}\n  ) {\n    ...PRICE_SUMMARY_FIELDS @skip(if: $isFixedOnly)\n    __typename\n  }\n  __typename\n}\n\nfragment PRICE_SUMMARY_SUB_FIXED on Car {\n  priceSummarySubFixed: priceSummary(\n    priceConfigInput: {locale: $locale, name: "sub_fixed", priceDates: $priceDates, roundingStrategy: alwaysRound, taxation: $taxation, mileage: $mileage, contractLength: $contractLength, downpayment: $downpayment, variableReferences: [{name: "customerType", value: $customerType}, {name: "CompanyCarMileage", value: $companyCarMileage}]}\n  ) {\n    ...PRICE_SUMMARY_FIELDS\n    __typename\n  }\n  __typename\n}\n',
}

response = requests.post(
    "https://www.volvocars.com/api/graphql", headers=headers, json=json_data
)

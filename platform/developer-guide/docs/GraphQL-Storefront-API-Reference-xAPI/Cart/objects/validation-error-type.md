# ValidationErrorType ==~object~==

The `ValidationErrorType` represents a validation error encountered during a specific operation or process. 

## Fields

| Field                                  | Description                                                                                              |
|----------------------------------------|----------------------------------------------------------------------------------------------------------|
| `errorCode`  ==String==                | The error code associated with the validation error.                                                       |
| `errorMessage`  ==String==             | The error message describing the validation error.                                                         |
| `objectId`  ==String==                 | The ID of the object that encountered the validation error.                                                |
| `objectType`  ==String==               | The type or category of the object that encountered the validation error.                                  |
| `errorParameters` [ ==ErrorParameterType== ](error-parameter-type.md) | A list of error parameters providing additional information about the validation error, if available. |

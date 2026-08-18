# VideoType ==~object~==

This type represents a video entity with its associated metadata and properties.

## Fields

| Field                        	| Description                                                                                        	|
|------------------------------	|----------------------------------------------------------------------------------------------------	|
| `name` ==String!==         	| The name of the video.                                                                             	|
| `description` ==String==   	| The description of the video.                                                                        	|
| `uploadDate` ==DateTime==  	| The date and time when the video was uploaded.                                                     	|
| `thumbnailUrl` ==String==  	| The URL of the thumbnail image associated with the video.                                         	|
| `contentUrl` ==String==    	| The URL of the video file.                                                                        	|
| `embedUrl` ==String==      	| The embeddable URL of the video, which can be usedto embed the video in webpages or applications.     |
| `duration` ==String==      	| The duration of the video.                                                                           	|
| `cultureName` ==String==   	| The language associated with the video.                                                            	|
| `ownerId` ==String==       	| The Id of the owner of the video.                                                                    	|
| `ownerType` ==String==     	| The type of the owner of the video.                                                                	|
| `sortOrder` ==Int!==       	| The sort order of the video in a list.                                                               	|


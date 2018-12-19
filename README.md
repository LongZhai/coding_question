Search 

Returns json data about the search function return. 

URL

/api/search/<string:search_input >

Method:

GET

URL Params

Required:

search_input=[String]

Success Response:

Code: 200 
Content: 
{

	"query_text": "time to engage",
    "number_of_occurrences": 1,
    "occurrences": [
        {
            "line": 43,
            "start": -8,
            "end": 7,
            "in_sentence": "This is no time to engage in the luxury of cooling off or to take the tranquilizing drug of gradualism"
        }
    ]
}

negative number means your search input is separated into to two lines;
 the first part will be at the end of the indicated line(in this sample--> "line": 43,) and the second part will be 
 at the beginning of the next line
 
 content sample indicates "time to engage" occurrences once, stating at the last 8th characters of 
 line 43 and ending at 7th characters of line 44



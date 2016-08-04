var express = require('express'),
    request = require('request'),
    bodyParser = require('body-parser'),
    app = express();

var myLimit = typeof(process.argv[2]) != 'undefined' ? process.argv[2] : '100kb';
console.log('Using limit: ', myLimit);

app.use(bodyParser.json({limit: myLimit}));

app.all('*', function (req, res, next) {

    // Set CORS headers: allow all origins, methods, and headers: you may want to lock this down in a production environment
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Methods", "GET, PUT, PATCH, POST, DELETE");
    res.header("Access-Control-Allow-Headers", req.header('access-control-request-headers'));

    if (req.method === 'OPTIONS') {
        // CORS Preflight
        res.send();
    } else {
        var apiType = req.header("api-Type");
        if (!apiType)
        {
            console.error('error: ' + 'Not proper request.');
        }

        var targetURL = req.header('Target-URL');
        if (!targetURL) {
            res.send(500, { error: 'There is no Target-Endpoint header in the request' });
            return;
        }

        if( apiType == 'TmapApi')
        {
            apiQuery = req.url.replace("/", "");
            //apiQuery.replace("/", "");
            console.log(apiQuery);
            console.log(targetURL)
            request({ url: targetURL + apiQuery,
            method: req.method, 
            headers: {
                'Content-Type' : req.header('Content-Type'),
                'X-Naver-Client-Id' : req.header('X-Naver-Client-Id'),
                'X-Naver-Client-Secret' : req.header('X-Naver-Client-Secret'),
                rejectUnauthorized:false 
                }},
                function (error, response, body) {
                    if (error) {
                        console.error('error: ' + error + response + body);
                    }
                    console.log(body);
                }).pipe(res);
        }
        else if( apiType == 'NaverApi')
        {
            apiQuery = req.url.replace("/", "");
            //apiQuery.replace("/", "");
            console.log(apiQuery);
            console.log(targetURL)
            request({ url: targetURL + apiQuery,
            method: req.method, 
            headers: {
                'Content-Type' : req.header('Content-Type'),
                'X-Naver-Client-Id' : req.header('X-Naver-Client-Id'),
                'X-Naver-Client-Secret' : req.header('X-Naver-Client-Secret'),
                rejectUnauthorized:false 
                }},
                function (error, response, body) {
                    if (error) {
                        console.error('error: ' + error + response + body);
                    }
                    console.log(body);
                }).pipe(res);
        }
        else
        {
            console.error('error: ' + 'Unknown Api type');
        }
    }
});

app.set('port', process.env.PORT || 3000);

app.listen(app.get('port'), function () {
    console.log('Proxy server listening on port ' + app.get('port'));
});
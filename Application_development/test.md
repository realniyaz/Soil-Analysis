## Testing the API:
```
Run the Flask app:
python app.py
```

## Use Postman or cURL to test the API:
```
curl -X POST -F "file=@path_to_image.jpg" http://127.0.0.1:5000/analyze
```

## Response:

```
{
    "soil_type": "Loamy"
}
```

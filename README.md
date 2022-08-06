![Python](https://img.shields.io/badge/bcra_api_collector-v1.0.0-orange)
![Python](https://img.shields.io/badge/platform-linux--64%7Cwin--64-lightgrey)

# bcra-api
Project that gathers information from BCRA API
Stack:
 - Python
 - Prometheus
 - Grafana

<img src="doc/diagram.png" />


### query BCRA API

```bash
curl https://api.estadisticasbcra.com/usd -H "Accept: application/json" -H "Authorization: Bearer {token}"
```

## References 
- https://estadisticasbcra.com/api/documentacion

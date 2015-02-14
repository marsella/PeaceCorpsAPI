
# Peace Corp Country-Regions-REST-API Wrapper

This is a wrapper for the [PCCR REST
API](https://github.com/PeaceCorps/Countries-Regions-REST-API) to produce more
machine-readable output.

Produces `Opportunity` objects from the JSON response for a valid API request.

| Name | Type   | Description |
------|---------|--------------|
| id   | int    | Unique country identifier |
| name | string | human-readable country name
| slug | string | Unique country identifier |
| region | string | unique region identifier |
| current | bool | whether program is active|
| volunteers | int | num of PC volunteers |
| pcr | bool | PC Response available |
| sectors | list of bool | peace corps program sectors |
| languages | list of string | languages spoken |

Note that all strings are Unicode.


## Wrapper Details
Most of the documentation on the original API still holds true. These are
details that have been made more machine-readable by the wrapper.
### Sector
The current enumeration of sectors is
  1. Agriculture
  2. Community
  3. Education
  4. Environment
  5. Health
  6. Youth 

The sector field returns a bitlist that corresponds to this enumeration.
For example, 
```
sectors: "<p> Agriculture, Community Development, Education, Environment,Youth Development</p> "
```
becomes
```
sectors: [1,1,1,1,0,1]
```

The enumeration is public.

### Languages
Produces a list of languages. This isn't quite perfect.
Ex. 
```
languages: "Garifuna, Q'eqchi, Kriol, Mopan, and Spanish"
```
becomes
```
languages: ["Garifuna", "Q'eqchi", "Kriol", "Mopan", "Spanish"]
```

However,
```
languages: "Vincentian/Grenadian dialect and French Creole, also known as 
      Kweyol"
```
becomes
```
languages: ["Vincentian/Grenadian dialect", "French Creole", "also known as
      Kweyol"]
```
This is a known issue and more advanced language processing is required.


Made at [ID Hack 2015](idhack.developersfordevelopment.org). 



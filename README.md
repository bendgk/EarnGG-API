# EarnGG-API

Easy to use python implementation of the EarnGG developer API

### Prerequisites

python 2.7.x - https://www.python.org/downloads/

```
linux: sudo apt-get install python
```
### Usage
**Substitute your api key and secret key into their respective positions.**

**Get current balance**
```
balance = get_balance()
```

**Gamble**
- returns if you won the gamble as a boolean

```
print roll(10, 2)
>>> "true"
print roll(10, 2)
>>> "false
```

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

# TempMailApi

Friendly Wrapper for Temp Mail Api (https://market.mashape.com/Privatix/temp-mail).

# Installation

`pip install tempmailapi`
# Usage:
## Initialization
``` 
from tempmailapi import TempMailApi
api = TempMailApi(<your_token>)
```

## Methods:
Get disponible domains:
```
api.get_domains()
```


Get emails from an adress:
```
api.get_emails(<your email>)
```

Get attachment from an email:
```
api.get_message_attachments(<message id>)
```

Get specific message:
```
api.get_one_message(<message id>)
```

Get source from specific message:
```
api.get_source_message(<message id>)
```

Get delete specific message:
```
api.delete_message(<message id>)
```


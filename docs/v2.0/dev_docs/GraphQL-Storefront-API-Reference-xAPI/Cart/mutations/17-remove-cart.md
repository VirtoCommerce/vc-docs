# RemoveCart
This mutation allows you to remove a cart.

## Query

```json
mutation ($command:InputRemoveCartType!)
{
    (command: $command)
}
```

## Variables

```
"command": {
    "cartId": "7777-7777-7777-7777"
}
```
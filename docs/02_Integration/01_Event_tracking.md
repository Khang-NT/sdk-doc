# Track an event
```java
void onPurchased() {
    JSONObject eventProps = new JSONObject();
    eventProps.put("item", 1234);
    UserKit.getInstance().track("purchase", eventProps);
}
```
```swift
func onPurchased() {
   let eventProps = ["item": 1234];
   UserKit.mainInstance().track("purchase", eventProps);
}
```

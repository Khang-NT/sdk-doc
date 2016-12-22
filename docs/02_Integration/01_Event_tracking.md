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
Event property types are those which json format allowed, they are `String`, `Boolean`, `Array`, and `null`. Property with multi type example:
```java
void doTrackEvent() {
    // Map is also supported.
    Map<String, Object> eventProps = new HashMap<>();
    eventProps.put("String", "aString");
    eventProps.put("Double", 123.456);
    eventProps.put("Array", Arrays.asList("List of any object", 1, true));
    UserKit.getInstance().track("test_event", eventProps);
}
```
```swift
let eventProps = [
    "String": "aString",
    "Double": 123.456,
    "Array": ["List of any object", 1, true]
]
UserKit.mainInstance().track("test_event", eventProps);
```

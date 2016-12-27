# Installation
-------
#### CocoaPods  

```swift
pod 'UserKit', :git => 'https://github.com/iamkaiwei/userkit-iOS-SDK.git'
```
#### Manual Installion    
Simply drag UserKit project as a subproject to X-Code

# Initialization
------
```swift
func application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool {
    UserKit.initialize("YOUR_USERKIT_TOKEN")
    return true
}

```

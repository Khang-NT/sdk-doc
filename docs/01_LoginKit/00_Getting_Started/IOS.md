# Installation
-------
## Using CocoaPods

Add the line below to your Podfile:

`pod 'UserKitIdentity', :git => 'https://github.com/iamkaiwei/userkit-iOS-SDK.git'`

If you are not familiar with CocoaPods, have a look at [CocoaPods Getting Started](https://guides.cocoapods.org/using/getting-started.html) page.

## Manually

You can also get the library by downloading the latest version from Github and copying it into your project.

# Initialization

In most case, it makes sense that you should initialize `UserKitIdentity` in `application(_:didFinishLaunchingWithOptions:)`. To initialize the library, first `import UserKitIdentity` and then call `UserKitIdentity.initialize(token:)` with your project token as its argument. Once you've called this method, you can access your instance throughout the rest of your application with `mainInstance()`.

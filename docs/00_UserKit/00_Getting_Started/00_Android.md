Latest version:&nbsp;&nbsp;&nbsp;&nbsp;[![Download](https://api.bintray.com/packages/mstage/mStage-SDK/UserKit-SDK/images/download.svg) ](https://bintray.com/mstage/mStage-SDK/UserKit-SDK/_latestVersion)<br>
Build status:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Build status](https://circleci.com/gh/jupitervn/userKit-Android-SDK/tree/master.svg?style=shield&circle-token=0cb9923a82f369171f87d827bbc497e11b495e6d)
# Installation
-------
#### Gradle config:
```gradle
repositories {
    jcenter()
}
dependencies {
    compile 'com.mstage.userkit:sdk:$latest_version$'
}
```
#### AndroidManifest.xml
```xml
<uses-permission android:name="android.permission.INTERNET"/>

<application
    android:name=".MainApplication"
    ...>
    <meta-data android:name="USER_KIT_API_TOKEN" android:value="your_api_token_here" />

</application>
```
#### Initialization
```java
public class MainApplication extends Application {
    @Override
    public void onCreate() {
        UserKit.init(this);
        // Or using UserKit.init(this, "YOUR_API_TOKEN");
        // In case you haven't defined api token in AndroidManifest.xml
    }
}
```

Latest version:&nbsp;&nbsp;&nbsp;&nbsp;[![Download](https://api.bintray.com/packages/mstage/mStage-SDK/LoginKit-SDK/images/download.svg) ](https://bintray.com/mstage/mStage-SDK/LoginKit-SDK/_latestVersion)<br>
Build status:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Build status](https://circleci.com/gh/jupitervn/userKit-Android-SDK/tree/master.svg?style=shield&circle-token=0cb9923a82f369171f87d827bbc497e11b495e6d)
# Installation
-------
#### Gradle:
```
repositories {
    jcenter()
}
dependencies {
    compile 'com.mstage.userkit:identity:$latest_version$'
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
```Java
public class MainApplication extends Application {
    @Override
    public void onCreate() {
        LoginKit.init(this);
        // Or LoginKit.init(Context, USER_KIT_API_TOKEN)
        // In case you haven't defined api token in AndroidManifest.xml
    }
}

```

# Basic tutorials
----------
## Logging
Logging is disabled by default. To show/hide logs of `LoginKit`, just add some lines to your code:
```java
// import userkit.sdk.identity.Logging;
    // show log
    Logging.enable();
    // hide log
    Logging.disable();
```
## Java concurrency support using RxJava2:
```java
void doResetPassword(String email) {
    LoginKit.getInstance().resetPassword(email)
        .subscribeOn(Schedulers.io())
        .observeOn(AndroidSchedulers.mainThread())
        .subscribe(() -> Toast.makeText(this, "Reset password success", Toast.LENGTH_SHORT).show(),
            Throwable::printStackTrace);
}
```
## Lambda expression friendly
If you don't like `Observer` pattern, you can easily define callback functions
which was designed to friendly with Java 8 Lambda expression:
```java
void doResetPassword(String email) {
    LoginKit.getInstance().resetPassword(email,
        () -> Toast.makeText(this, "Reset password success", Toast.LENGTH_SHORT).show(),
        Throwable::printStackTrace);
}
```
#### Notice that
> This job will be scheduled to run in IO thread pool (`Schedulers.io()`), and will try to call back the consumer - `onSuccess` in the current thread (the thread call `resetPassword`), if can't, `onSuccess` will call back on **main thread**.

And the same thing with all API has callback function.

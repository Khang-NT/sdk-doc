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
#### Note:
> This job won't run until you call `subscribe()`.

If you want to run the request immediately and ignore the result, try it:
```java
LoginKit.getInstance().resetPassword(email)
        .subscribeOn(Schedulers.io())
        .subscribe();
```
Read more about [`RxJava`](https://github.com/ReactiveX/RxJava/wiki).

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
## Handling errors
React with specific `Exception` case is one of the most important parts in programming.
`LoginKit` make it simply to handle, if the error encountered is:
  * `IdentityException`: you made a bad request.
  You can print it into `Logcat` to get more detail. A convenient that you can know exactly
  what sort of error occurred, using `IdentityException.getIdentityError`.
  * `IOException`: maybe due to networking, the connection to server is broken during the request.
  * All other exceptions are of kind UNKNOWN, read the stack trace carefully.

Assume that we are going to create new account with email and password,
there are some exceptions that we must handle, such as:
  * Email is invalid or already exists.
  * Upload avatar failed due to networking.
  
Now let see how we can handle it:
```java
LoginKit.getInstance().signUpNewProfile("hello@world.com", "123abc", false, null,
        accountInfo -> {
            Log.d(TAG, "Register account success: " + accountInfo);
        },
        error -> {
            error.printStackTrace();
            if (error instanceOf IdentityException) {
                switch(((IdentityException) error).getIdentityError()) {
                    case EMAIL_EXIST:
                        Toast.makeText(this, "Email exist", Toast.LENGTH_SHORT).show();
                        break;
                    case INVALID_EMAIL_OR_PASSWORD:
                        Toast.makeText(this, "Invalid Email or Password", Toast.LENGTH_SHORT).show();
                        break;
                }
            } else if (error instanceOf IOException) {
                // A network error happened
            } else {
                throw Exceptions.propagate(error);
            }
        });
```

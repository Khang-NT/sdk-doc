<center>
<a href="https://bintray.com/mstage/mStage-SDK/LoginKit-SDK/_latestVersion"><img src="https://api.bintray.com/packages/mstage/mStage-SDK/LoginKit-SDK/images/download.svg"></img></a> <a href="#"><img src="https://circleci.com/gh/jupitervn/userKit-Android-SDK/tree/master.svg?style=shield&circle-token=0cb9923a82f369171f87d827bbc497e11b495e6d"></img></a>
</center>

# Installation
-------
#### Gradle:
Place `UserKitIdentity` dependency into your `build.gradle` in app module and make sure that `jcenter()`
is added to `repositories` section at project level `build.gradle` file.

```gradle
repositories {
    jcenter()
}
dependencies {
    compile 'com.mstage.userkit:identity:$latest_version$'
}
```

#### AndroidManifest.xml
It is optional step, that `UserKit` will find `USER_KIT_API_TOKEN`meta data
in `AndroidManifest.xml` file, then you needn't to specify `USER_KIT_API_TOKEN`
again when you [initialize](#initialization) `UserKit` instance.

```xml
<uses-permission android:name="android.permission.INTERNET"/>

<application
    android:name=".MainApplication"
    ...>
    <meta-data android:name="USER_KIT_API_TOKEN" android:value="your_api_token_here" />

</application>
```
Permission `android.permission.INTERNET` is also required.

#### Initialization
In most case, it makes sense that you should initialize `UserKitIdentity` when your `Application`
create, and you just add one line to your code:

```Java
public class MainApplication extends Application {
    @Override
    public void onCreate() {
        UserKitIdentity.init(this);
        // Or UserKitIdentity.init(Context, USER_KIT_API_TOKEN)
        // In case you haven't defined api token in AndroidManifest.xml
    }
}

```

# Tutorials
----------
## Logging
Print log is useful to debug your app, but strongly recommended that you shouldn't
show any log in release product. Logging is disabled by default in `UserKitIdentity`,
to show/hide logs just add some lines to your code:
```java
// import userkit.sdk.identity.Logging;
// show log
Logging.enable();
// hide log
Logging.disable();
```
## Java concurrency support using RxJava2:
You can observe result and [handle errors](#handling-errors) of all APIs in `UserKitIdentity` SDK
with [`ReactiveX`](http://reactivex.io/) concept.
```java
UserKitIdentity.getInstance().resetPassword("hello@world.com")
        .subscribeOn(Schedulers.io())
        .observeOn(AndroidSchedulers.mainThread())
        .subscribe(() -> Toast.makeText(this, "Reset password success", Toast.LENGTH_SHORT).show(),
            Throwable::printStackTrace);
```
#### Note:
> This job won't run until you call `subscribe()`.

If you want to run the request immediately and ignore the result, you can subscribe
without specify any callback.
```java
UserKitIdentity.getInstance().resetPassword(email)
        .subscribeOn(Schedulers.io())
        .subscribe();
```
Read more about [`RxJava`](https://github.com/ReactiveX/RxJava/wiki).

## Lambda expression friendly
If you don't like `Observer` pattern, you can easily define callback functions
which was designed to friendly with Java 8 Lambda expression:
```java
void doResetPassword(String email) {
    UserKitIdentity.getInstance().resetPassword(email,
        () -> Toast.makeText(this, "Reset password success", Toast.LENGTH_SHORT).show(),
        Throwable::printStackTrace);
}
```
#### Notice that
> This job will be scheduled to run in IO thread pool (`Schedulers.io()`), and will try to call back the consumer - `onSuccess` in the current thread (the thread call `resetPassword`), if can't, `onSuccess` will call back on **main thread**.

And the same thing with all API has callback function.
## Handling errors
React with specific `Exception` case is one of the most important parts in programming.
`UserKitIdentity` make it simply to handle, if the error encountered is:
  * `IdentityException`: somethings wrong with your request.
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
UserKitIdentity.getInstance().signUpNewProfile("hello@world.com", "123abc", false, null,
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

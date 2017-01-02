{% method %}
## Sign up new account
-------------
User can create new account with `email`, `password` and store a specific profile for this account.
Try it:

{% sample lang="Android" %}
```java
ProfileProperties profileProps = ImmutableProfileProperties.builder()
        .name("John")  
        .avatar(avatarFile)
        .putProperties("account_type", "free")
        .putProperties("is_male", true)
        .putProperties("age", 21)
        .build();
LoginKit.getInstance()
        .signUpNewProfile("hello@world.com", "123abc", false, profileProps)
        .subscribeOn(Schedulers.io())
        .observeOn(AndroidSchedulers.mainThread())
        .subscribe(accountInfo -> {
            Log.d(TAG, "Register account success: " + accountInfo);
        }, Throwable::printStackTrace);
```

{% sample lang="IOS" %}
```swift
// updating...
```

{% endmethod %}

After User created an account, now they can use it to login, let move to next section.

{% method %}
## Sign in using _email_ and _password_
----------

{% sample lang="Android" %}
```java
LoginKit.getInstance().loginWithEmailAndPassword("hello@world.com", "123abc",
        accountInfo -> {
            Log.d(TAG, "Login success: " + accountInfo);
        }, Throwable::printStackTrace);
```

{% sample lang="IOS" %}
```swift
// updating...
```

{% endmethod %}
After that you can manage user's profiles using [AccountManager](02_Account_Manager.md). <br>
Beside login using email and password, `LoginKit` also supports authenticate with social account from `Facebook` and `Google`.

## Sign in using _Facebook_ token
----------
```java
LoginKit.getInstance().loginFacebookAccount("place Facebook access token here",
        accountInfo -> {
            Log.d(TAG, "Login using Facebook auth token success: " + accountInfo);
        }, Throwable::printStackTrace);
```
```swift
// updating...
```
## Sign in using _Google plus_ token
---------
```java
LoginKit.getInstance().loginGooglePlusAccount("place Google+ auth token here",
        accountInfo -> {
            Log.d(TAG, "Login using Google+ auth token success: " + accountInfo);
        }, Throwable::printStackTrace);
```
```swift
// updating...
```
## Reset password of account created by email
--------
Add feature _"Reset password"_ into your app, using `LoginKit.resetPassword` api:
```java
LoginKit.getInstance().resetPassword("hello@world.com",
        () -> {
            Toast.makeText(this, "Email reset password was sent to your inbox.", Toast.LENGTH_SHORT).show();
        }, error -> {
            // encounter an error
            error.printStackTrace();
        })
```
```swift
// updating...
```

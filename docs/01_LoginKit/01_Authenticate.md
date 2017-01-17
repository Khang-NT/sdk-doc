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
UserKitIdentity.getInstance()
        .signUpNewProfile("hello@world.com", "123abc", false, profileProps)
        .subscribeOn(Schedulers.io())
        .observeOn(AndroidSchedulers.mainThread())
        .subscribe(accountInfo -> {
            Log.d(TAG, "Register account success: " + accountInfo);
        }, Throwable::printStackTrace);
```

{% sample lang="IOS" %}

```swift
let profile = UserKitIdentityProfile(json: ["name": "John", "avatar": avatarFile, "account_type": "free", "is_male": true, "age": 21])
UserKitIdentity.mainInstance().signUpNewProfile("hello@world.com", password: "123abc", profile: profile, customProperties: [:], successBlock: { authenticationModel in
        //your code
}, failureBlock: { autheticationErrorModel in
        //your code
})

```

{% endmethod %}

After User created an account, now they can use it to login, let move to next section.

{% method %}

## Sign in using _email_ and _password_
----------

{% sample lang="Android" %}

```java
UserKitIdentity.getInstance().loginWithEmailAndPassword("hello@world.com", "123abc",
        accountInfo -> {
            Log.d(TAG, "Login success: " + accountInfo);
        }, Throwable::printStackTrace);
```

{% sample lang="IOS" %}

```swift
UserKitIdentity.mainInstance().loginWithEmailAndPassword("hello@world.com", password: "123abc", successBlock: { authenticationModel in
        //your code
}, failureBlock:  { autheticationErrorModel in
        //your code
})
```

{% endmethod %}

After that you can manage user's profiles using [AccountManager](02_Account_Manager.md). <br>
Beside login using email and password, `UserKitIdentity` also supports authenticate with social account from `Facebook` and `Google`.

{% method %}

## Sign in using _Facebook_ token
----------

{% sample lang="Android" %}

```java
UserKitIdentity.getInstance().loginFacebookAccount("place Facebook access token here",
        accountInfo -> {
            Log.d(TAG, "Login using Facebook auth token success: " + accountInfo);
        }, Throwable::printStackTrace);
```

{% sample lang="IOS" %}

```swift
// updating...
```

{% endmethod %}

{% method %}

## Sign in using _Google plus_ token
---------

{% sample lang="Android" %}

```java
UserKitIdentity.getInstance().loginGooglePlusAccount("place Google+ auth token here",
        accountInfo -> {
            Log.d(TAG, "Login using Google+ auth token success: " + accountInfo);
        }, Throwable::printStackTrace);
```

{% sample lang="IOS" %}

```swift
// updating...
```

{% endmethod %}

{% method %}

## Reset password of account created by email
--------
Add feature _"Reset password"_ into your app, using `UserKitIdentity.resetPassword` api:

{% sample lang="Android" %}

```java
UserKitIdentity.getInstance().resetPassword("hello@world.com",
        () -> {
            Toast.makeText(this, "Email reset password was sent to your inbox.", Toast.LENGTH_SHORT).show();
        }, error -> {
            // encounter an error
            error.printStackTrace();
        })
```

{% sample lang="IOS" %}

```swift
// updating...
```

{% endmethod %}

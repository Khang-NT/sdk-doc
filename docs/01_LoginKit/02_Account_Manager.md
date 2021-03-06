
## Overview

{% method %}

Access `AccountManager` instance:

{% sample lang="Android" %}

```java
AccountManager accountManager = UserKitIdentity.getAccountManager();
```
> **Notice that** to use apis under `AccountManager`, you must ensure that
user already logged in, to check if user logged in or not, use `AccountManager.isLoggedIn()`
method.

{% sample lang="IOS" %}

```swift
let profileManager = UserKitIdentity.mainInstance().profileManager
```

{% endmethod %}

## Managing account profiles
With `UserKitIdentity`, every account can have multiple profiles. After `user` logged in,
you can access all profile of their account by using `ProfileManager.getAccountProfiles()`:

{% method %}

### Get all profiles

{% sample lang="Android" %}

```java
UserKitIdentity.getAccountManager().getAccountProfiles()
    .flatMap(listProfile -> Observable.from(listProfile))
    .subscribeOn(Schedulers.io())
    .subscribe(profile -> {
        // do on each profile
        Log.d("AccountProfile", profile.toString());
    }, Throwable::printStackTrace);
```

{% sample lang="IOS" %}

```swift
UserKitIdentity.mainInstance().profileManager.getProfile({ listProfile in
        //your code
}, failureBlock: { autheticationErrorModel in
        //your code
})
```

{% endmethod %}

{% method %}

### Create new profile
To create new profile for current account, use `AccountManager.createNewProfile()`.

{% sample lang="Android" %}

```java
// create vip profile for current account.
ProfileProperties profileProps = ImmutableProfileProperties.builder()
        .name("John")  
        .putProperties("account_type", "vip_account")
        .build();
UserKitIdentity.getAccountManager().createNewProfile(profileProps,
        newProfile -> Log.d("CreateProfile", "Success: " + newProfile));
```
After profile is created, `UserKitIdentity` uses it as activating profile by default, you
can check the current active profile via `AccountManager.getCurrentActiveProfileId()`.
{% sample lang="IOS" %}

```swift
let profile = UserKitIdentityProfile(json: ["name": "John", "account_type": "vip_account"])!
UserKitIdentity.mainInstance().profileManager.createProfile(profile, customProperties: [:], successBlock: { listProfile in
        //your code
}, failureBlock: { autheticationErrorModel in
        //your code
})
```

{% endmethod %}

{% method %}

### Switch to another profile

Then in case you want to switch to another available profile, `UserKitIdentity` has method
to switch to any profile with specific `id`.

{% sample lang="Android" %}
```java
UserKitIdentity.getAccountManager().switchToProfile("another_profile_id",
        newAuthToken -> System.out.println(newAuthToken),
        Throwable::printStackTrace);
```
After switching profile succeed, `AccountManager.getCurrentActiveProfileId()` should
return the value `"another_profile_id"`.

{% sample lang="IOS" %}

```swift
UserKitIdentity.mainInstance().profileManager.switchProfile("another_profile_id", successBlock: { newAuthToken in
        //your code
}, failureBlock: { autheticationErrorModel in
        //your code
})
```

{% endmethod %}

{% method %}

### Update profile
Update profile is essential when User want to update some property such as avatar, name.

{% sample lang="Android" %}

Like [create profile](#create-new-profile), you can specify an `ProfileProperties`
to update current activate profile.
```java
ProfileProperties profileProps = ImmutableProfileProperties.builder()
        .name("New name")  
        .avatar(new File("/path/to/new/avatar"))
        .build();
UserKitIdentity.getAccountManager().updateProfile(profileProps)
        .subscribe(
            accountProfile -> Log.d("UpdateProfile", accountProfile.toString()),
            Throwable::printStackTrace);
```

If you only want to update avatar of current account, you can use `updateAvatar()` method, try it:
```java
UserKitIdentity.getAccountManager().updateAvatar(new File("/path/to/new/avatar"),
        imageInfoList -> System.out.println(imageInfoList),
        Throwable::printStackTrace)
```

{% sample lang="IOS" %}

```swift
UserKitIdentity.mainInstance().profileManager.updateProfile(profileId, customProperties: ["name": "New name", "avatar" : newAvatarFile], successBlock: { profile in
        //your code
}, failureBlock: { authenticationErrorModel in
        //your code
})
```

{% endmethod %}

{% method %}

### Delete profile
In addition of [create profile](#create-new-profile) and [update profile](#update-profile),
you can delete profile of an account by using `deleteProfile`.

{% sample lang="Android" %}

Method requires a specific `ID` of profile to be deleted.
```java
UserKitIdentity.getAccountManager().deleteProfile("profile_id",
        () -> Log.d("DeleteProfile", "Delete profile succeed"),
        Throwable::printStackTrace);
```

{% sample lang="IOS" %}

```swift
UserKitIdentity.mainInstance().profileManager.deleteProfile(profileId, successBlock: { resultDictionary in
        //your code
}, failureBlock: { authenticationErrorModel in
        //your code
})
```

{% endmethod %}

## Get account properties

{% method %}

{% sample lang="Android" %}

{% sample lang="IOS" %}

```swift
UserKitIdentity.mainInstance().profileManager.getProfile(successBlock: { properties in
    //your code
}, failureBlock: { error in
    //your code
})
```

{% endmethod %}

## Update account properties

{% method %}

{% sample lang="Android" %}

{% sample lang="IOS" %}

```swift
UserKitIdentity.mainInstance().profileManager.updateProfile(["pin": "1234"], successBlock: { properties in
    //your code
}, failureBlock: { error in
    //your code
})
```

{% endmethod %}

## Change password

{% method %}

Change password is an important feature to help User protect their account,
`AccountManager` provides API to change password of current account, remind
again that `AccountManager` only works with the account currently logged in. <br><br>

User also need to present their old password if they want to change password,
it's because of security reason.

{% sample lang="Android" %}

You will get error if old password is not match, or new password invalid,...
To handle these exceptions, see [Handling errors](00_Getting_Started/Android.md#handling-errors).
```java
UserKitIdentity.getAccountManager().changePassword("old_password", "new_password")
        .subscribe(
            () -> Toast.makeText(getContext(), "Change password succeed, now you can login with new password"),
            error -> handleError(error);    // handle errors
        );
```

{% sample lang="IOS" %}

```swift
UserKitIdentity.mainInstance().profileManager.changePassword("old_passord", newPassword: "new_password", successBlock: { object in
        //your code
}, failureBlock: { authenticationErrorModel in
        //your code
})
```

{% endmethod %}

## Install instruction for Web
asd asd
asd
```javascript
/**
 @constructor
 @abstract
 */
var Animal = function() {
    if (this.constructor === Animal) {
      throw new Error("Can't instantiate abstract class!");
    }
    // Animal initialization...
};

/**
 @abstract
 */
Animal.prototype.say = function() {
    throw new Error("Abstract method!");
}
```

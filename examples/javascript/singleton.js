class Singleton {
    constructor() {
        if (Singleton._instance)
            throw new Error("instantiated already");

        Singleton._instance = this;
    }
    //some code
    getData() {
        return this.Data;
    }

    setData(data) {
        this.Data = data;
    }
}

let c = new Singleton();
console.log(c.setData(12));
console.log(c.getData());



const test = () => {
    this.c = 22;
    this.a = function () {
        console.log("ok");
    }
}

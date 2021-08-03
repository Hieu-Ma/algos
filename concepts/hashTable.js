function hasStringToInt(s) {
   return 5;
}

class HashTable {

   table = new Array(100)
   
   // hash function
   
   setItem = (key, value) => {
      const idx = hasStringToInt(key);
      this.table[idx] = value;
   };

   getItem = (key) => {
      const idx = hasStringToInt(key)
      return this.table[idx];
   };

}

const myTable = new HashTable();
myTable.setItem("firstName", "bob");
myTable.getItem("firstName");
console.log(myTable.getItem("firstName"));
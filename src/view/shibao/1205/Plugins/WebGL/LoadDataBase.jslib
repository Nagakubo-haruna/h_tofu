mergeInto(LibraryManager.library, {

  ConsoleLog: function(message) {
    console.log("%c" + Pointer_stringify(message), "color:blue");
  },

});

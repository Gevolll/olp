// // 获取 Cookie
// export function getCookie(name) {
//   var arr, re = new RegExp("(^| )"+name+"=([^;]*)(;|$)");
//   if (arr = document.cookie.match(re)) {
//     return arr[2];
//   } else {
//     return null;
//   }
// }
//
// // 设置 Cookie，需要添加到 Vue 实例，方便全局调用
// export function setCookie(name, value, expiredays) {
//   var exdate = new Date();
//   exdate.setDate(exdate.getDate()+expiredays);
//   document.cookie = name+"="+escape(value)+((expiredays==null) ? "" : ";expires="+exdate.toGMTString());
// }
//
// // 删除 Cookie
// export function delCookie(name) {
//   var exp = new Date()
//   exp.setTime(exp.getTime() - 1);
//   var cvar = getCookie(name);
//   if(cvar != null) {
//     document.cookie = name+"="+cvar+";expires="+exp.toGMTString();
//   }
// }

module.exports = {
  methods: {
    getCookie: function (name) {
      var arr, re = new RegExp("(^| )"+name+"=([^;]*)(;|$)");
      if (arr = document.cookie.match(re)) {
        return arr[2];
      } else {
        return null;
      }
    },
    setCookie: function (name, value, expiredays) {
      var exdate = new Date();
      exdate.setDate(exdate.getDate()+expiredays);
      document.cookie = name+"="+escape(value)+((expiredays==null) ? "" : ";expires="+exdate.toGMTString());
    },
    delCookie: function (name) {
      var exp = new Date()
      exp.setTime(exp.getTime() - 1);
      var cvar = getCookie(name);
      if(cvar != null) {
        document.cookie = name+"="+cvar+";expires="+exp.toGMTString();
      }
    }
  },
  install: function (Vue, options) {
    Vue.prototype.$getCookie = this.methods.getCookie;
    Vue.prototype.$setCookie = this.methods.setCookie;
    Vue.prototype.$delCookie = this.methods.delCookie;
  }
}

// alite XMLHttpRequest wrapper (https://github.com/chrisdavies/alite)
function alite(e){function t(){}function a(e){var t=e&&e.responseText,a=/^[\{\[]/.test(t);return a?JSON.parse(t):t}return new Promise(function(n,r){var s=(e.xhr||t)()||new XMLHttpRequest,o=e.data;if(s.onreadystatechange=function(){4==s.readyState&&(s.status>=200&&s.status<300?n(a(s)):r(a(s)),(alite.ajaxStop||t)(s,e))},s.open(e.method,e.url),!e.raw&&s.setRequestHeader("Content-Type","application/json"),e.headers)for(var i in e.headers)s.setRequestHeader(i,e.headers[i]);(alite.ajaxStart||t)(s,e),(e.ajaxStart||t)(s),s.send(e.raw?o:o?JSON.stringify(o):void 0)})}"undefined"!=typeof module&&module.exports&&(module.exports=alite);

(window.webpackJsonp=window.webpackJsonp||[]).push([[10],{296:function(e,t,n){"use strict";n.r(t);var a=n(247),i=n(85),s=n(86),r=n(88),u=n(87),c=n(89),l=n(1),o=n.n(l),b=n(248),f=n.n(b),h=function(e){function t(e){var n;return Object(i.a)(this,t),(n=Object(r.a)(this,Object(u.a)(t).call(this,e))).baseUrl="http://52.87.206.237:8000/",n.subscribe=function(e){e.preventDefault(),console.log("Subscribing "+n.state.subMail),f.a.post(n.baseUrl+"subscribe/",{email:n.state.subMail}).then(function(){alert("Thanks for subscribing!")}).catch(function(){alert("There was an error subscribing, please try again later")})},n.handleChange=function(e){n.setState(Object(a.a)({},e.target.name,e.target.value))},n.state={subMail:"",unsubMail:""},n}return Object(c.a)(t,e),Object(s.a)(t,[{key:"componentDidMount",value:function(){window.open(this.baseUrl+"mail/")}},{key:"render",value:function(){return o.a.createElement("div",null)}}]),t}(l.Component);t.default=h}}]);
//# sourceMappingURL=10.71e1db4b.chunk.js.map
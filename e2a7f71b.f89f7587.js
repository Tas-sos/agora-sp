(window.webpackJsonp=window.webpackJsonp||[]).push([[13],{127:function(e,t,r){"use strict";r.r(t),t.default=r.p+"assets/images/login_0-7dad52210cfa78b6ded139156c82a1ba.png"},128:function(e,t,r){"use strict";r.r(t),t.default=r.p+"assets/images/login_1-c210c5ad50b1658d930cd638150b244e.png"},69:function(e,t,r){"use strict";r.r(t),r.d(t,"frontMatter",(function(){return o})),r.d(t,"metadata",(function(){return c})),r.d(t,"rightToc",(function(){return l})),r.d(t,"default",(function(){return b}));var n=r(2),a=r(6),i=(r(0),r(73)),o={id:"login",title:"Login Information"},c={unversionedId:"login",id:"login",isDocsHomePage:!1,title:"Login Information",description:"Agora there are two ways to login:",source:"@site/docs/login.md",permalink:"/agora-sp/docs/login"},l=[{value:"User categories",id:"user-categories",children:[{value:"Superadmin",id:"superadmin",children:[]},{value:"Admin.",id:"admin",children:[]},{value:"Resource Admin.",id:"resource-admin",children:[]},{value:"Observer",id:"observer",children:[]}]}],s={rightToc:l};function b(e){var t=e.components,o=Object(a.a)(e,["components"]);return Object(i.b)("wrapper",Object(n.a)({},s,o,{components:t,mdxType:"MDXLayout"}),Object(i.b)("p",null,"Agora there are two ways to login:"),Object(i.b)("ul",null,Object(i.b)("li",{parentName:"ul"},Object(i.b)("p",{parentName:"li"},"Basic authentication : Where user credentials are stored in the local database and verified from there.")),Object(i.b)("li",{parentName:"ul"},Object(i.b)("p",{parentName:"li"},"Authentication via third party proxy with multiply identity providers ( ",Object(i.b)("em",{parentName:"p"},"using Shibboleth")," ) : In this case, an external trusted provider authenticates the user."))),Object(i.b)("p",null,Object(i.b)("strong",{parentName:"p"},"All users except the ",Object(i.b)("em",{parentName:"strong"},"superuser")," will register and log in via the respective provider.")),Object(i.b)("table",null,Object(i.b)("thead",{parentName:"table"},Object(i.b)("tr",{parentName:"thead"},Object(i.b)("th",Object(n.a)({parentName:"tr"},{align:"center"}),Object(i.b)("img",{alt:"The Login Page",src:r(127).default})))),Object(i.b)("tbody",{parentName:"table"},Object(i.b)("tr",{parentName:"tbody"},Object(i.b)("td",Object(n.a)({parentName:"tr"},{align:"center"}),Object(i.b)("em",{parentName:"td"},"Login page"))))),Object(i.b)("table",null,Object(i.b)("thead",{parentName:"table"},Object(i.b)("tr",{parentName:"thead"},Object(i.b)("th",Object(n.a)({parentName:"tr"},{align:"center"}),Object(i.b)("img",{alt:"After successful login",src:r(128).default})))),Object(i.b)("tbody",{parentName:"table"},Object(i.b)("tr",{parentName:"tbody"},Object(i.b)("td",Object(n.a)({parentName:"tr"},{align:"center"}),Object(i.b)("em",{parentName:"td"},"First screen after a successful login"))))),Object(i.b)("h1",{id:"authentication-and-authorization"},"Authentication and Authorization"),Object(i.b)("p",null,"A new user who has just registered on Agora, acquires only the right of access to the service as an observer.\nThat is why it automatically enters the category of ",Object(i.b)("inlineCode",{parentName:"p"},"observer"),' users.\nTo grant more permissions, these it must be assigned by an "admin" or "superadmin" user.\nSee below the categories of users that exist as well as their respective rights.'),Object(i.b)("h2",{id:"user-categories"},"User categories"),Object(i.b)("h3",{id:"superadmin"},"Superadmin"),Object(i.b)("p",null,"Administers the whole system."),Object(i.b)("ul",null,Object(i.b)("li",{parentName:"ul"},"Profile                       : Can only see their own personal information."),Object(i.b)("li",{parentName:"ul"},"Resources                     : It can create/edit/delete resources for all Resource Organizations (without any restrictions)."),Object(i.b)("li",{parentName:"ul"},"Providers                     : It can create/edit/delete provider (without any restrictions)."),Object(i.b)("li",{parentName:"ul"},"Contact Information           : It can create/edit/delete Contact Information ",Object(i.b)("em",{parentName:"li"},"for all Providers")," (without any restrictions)."),Object(i.b)("li",{parentName:"ul"},"Resource Admins               : It can create/edit/delete and assign a resource admin to a resource."),Object(i.b)("li",{parentName:"ul"},"Users                         : It can edit/delete (without any restrictions)."),Object(i.b)("li",{parentName:"ul"},"Resource Settings             : It can create/edit/delete everywhere."),Object(i.b)("li",{parentName:"ul"},"Provider Settings             : It can create/edit/delete everywhere."),Object(i.b)("li",{parentName:"ul"},"Classification Settings       : It can create/edit/delete everywhere."),Object(i.b)("li",{parentName:"ul"},"User Settings -> Target Users : It can create/edit/delete everywhere.")),Object(i.b)("h3",{id:"admin"},"Admin."),Object(i.b)("p",null,"Allowed to do whatever a Resource Admin can do besides Delete."),Object(i.b)("ul",null,Object(i.b)("li",{parentName:"ul"},"Profile                       : Can only see their own personal information."),Object(i.b)("li",{parentName:"ul"},"Resources                     : It can create/edit resources for all Resource Organizations (without any restrictions)."),Object(i.b)("li",{parentName:"ul"},"Providers                     : It can create/edit provider (without any restrictions)."),Object(i.b)("li",{parentName:"ul"},"Contact Information           : It can create/edit Contact Information ",Object(i.b)("em",{parentName:"li"},"for all Providers")," (without any restrictions)."),Object(i.b)("li",{parentName:"ul"},"Resource Admins               : It can create/edit and assign a resource admin to a resource."),Object(i.b)("li",{parentName:"ul"},"Users                         : It can edit (without any restrictions)."),Object(i.b)("li",{parentName:"ul"},"Resource Settings             : It can create/edit everywhere."),Object(i.b)("li",{parentName:"ul"},"Provider Settings             : It can create/edit everywhere."),Object(i.b)("li",{parentName:"ul"},"Classification Settings       : It can create/edit everywhere."),Object(i.b)("li",{parentName:"ul"},"User Settings -> Target Users : It can create/edit everywhere.")),Object(i.b)("h3",{id:"resource-admin"},"Resource Admin."),Object(i.b)("ul",null,Object(i.b)("li",{parentName:"ul"},"Each Resource Admin belongs only to one provider"),Object(i.b)("li",{parentName:"ul"},"Each Resource Admin is allowed to edit delete update his own resources (i.e. Resources he/she created or given Rights too)"),Object(i.b)("li",{parentName:"ul"},"Each Resource Admin is allowed to apply to gain rights in other resources in his provider."),Object(i.b)("li",{parentName:"ul"},"Each Resource Admin is able also to approve or deny rights to other Resource Admins to his/her resource")),Object(i.b)("ul",null,Object(i.b)("li",{parentName:"ul"},"Profile                       : Can only see their own personal information."),Object(i.b)("li",{parentName:"ul"},"Resources                     : It can create ",Object(i.b)("em",{parentName:"li"},"new")," resources, but ",Object(i.b)("em",{parentName:"li"},"only for the Resource Organization to which it belongs"),"."),Object(i.b)("li",{parentName:"ul"},"My Resources                  : It can create ",Object(i.b)("em",{parentName:"li"},"new")," resources, but ",Object(i.b)("em",{parentName:"li"},"only for the Resource Organization to which it belongs"),"."),Object(i.b)("li",{parentName:"ul"},"Providers                     : It can only view \u03c4\u03bf\u03c5\u03c2 \u03c5\u03c0\u03ac\u03c1\u03c7\u03c9\u03bd providers."),Object(i.b)("li",{parentName:"ul"},"Contact Information           : It can create new Contact Information, but ",Object(i.b)("em",{parentName:"li"},"only for the Provider to which it belongs"),"."),Object(i.b)("li",{parentName:"ul"},"Resource Admins               : It can only view existing resource admins in the Resource Organization to which it belongs."),Object(i.b)("li",{parentName:"ul"},"Resource Settings             : It can only view."),Object(i.b)("li",{parentName:"ul"},"Provider Settings             : It can only view."),Object(i.b)("li",{parentName:"ul"},"Classification Settings       : It can only view."),Object(i.b)("li",{parentName:"ul"},"User Settings -> Target Users : It can only view.")),Object(i.b)("h3",{id:"observer"},"Observer"),Object(i.b)("blockquote",null,Object(i.b)("p",{parentName:"blockquote"},"Has Only view rights.")),Object(i.b)("ul",null,Object(i.b)("li",{parentName:"ul"},"Profile                       : Can only see their own personal information."),Object(i.b)("li",{parentName:"ul"},"Resources                     : It can only view ",Object(i.b)("strong",{parentName:"li"},"all entries"),"."),Object(i.b)("li",{parentName:"ul"},"Providers                     : It can only view ",Object(i.b)("strong",{parentName:"li"},"all entries"),"."),Object(i.b)("li",{parentName:"ul"},"Contact Information           : It can only view ",Object(i.b)("strong",{parentName:"li"},"all entries"),"."),Object(i.b)("li",{parentName:"ul"},"Resource Admins               : It can only view existing resource admins in the Resource Organization to which it belongs."),Object(i.b)("li",{parentName:"ul"},"Resource Settings             : It can only view."),Object(i.b)("li",{parentName:"ul"},"Provider Settings             : It can only view."),Object(i.b)("li",{parentName:"ul"},"Classification Settings       : It can only view."),Object(i.b)("li",{parentName:"ul"},"User Settings -> Target Users : It can only view.")))}b.isMDXComponent=!0},73:function(e,t,r){"use strict";r.d(t,"a",(function(){return u})),r.d(t,"b",(function(){return m}));var n=r(0),a=r.n(n);function i(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function o(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function c(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?o(Object(r),!0).forEach((function(t){i(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):o(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function l(e,t){if(null==e)return{};var r,n,a=function(e,t){if(null==e)return{};var r,n,a={},i=Object.keys(e);for(n=0;n<i.length;n++)r=i[n],t.indexOf(r)>=0||(a[r]=e[r]);return a}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(n=0;n<i.length;n++)r=i[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(a[r]=e[r])}return a}var s=a.a.createContext({}),b=function(e){var t=a.a.useContext(s),r=t;return e&&(r="function"==typeof e?e(t):c(c({},t),e)),r},u=function(e){var t=b(e.components);return a.a.createElement(s.Provider,{value:t},e.children)},p={inlineCode:"code",wrapper:function(e){var t=e.children;return a.a.createElement(a.a.Fragment,{},t)}},d=a.a.forwardRef((function(e,t){var r=e.components,n=e.mdxType,i=e.originalType,o=e.parentName,s=l(e,["components","mdxType","originalType","parentName"]),u=b(r),d=n,m=u["".concat(o,".").concat(d)]||u[d]||p[d]||i;return r?a.a.createElement(m,c(c({ref:t},s),{},{components:r})):a.a.createElement(m,c({ref:t},s))}));function m(e,t){var r=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var i=r.length,o=new Array(i);o[0]=d;var c={};for(var l in t)hasOwnProperty.call(t,l)&&(c[l]=t[l]);c.originalType=e,c.mdxType="string"==typeof e?e:n,o[1]=c;for(var s=2;s<i;s++)o[s]=r[s];return a.a.createElement.apply(null,o)}return a.a.createElement.apply(null,r)}d.displayName="MDXCreateElement"}}]);
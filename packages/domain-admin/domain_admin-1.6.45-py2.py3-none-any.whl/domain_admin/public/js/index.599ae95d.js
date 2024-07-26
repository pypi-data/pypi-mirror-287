import{H as U}from"./highlight-lib.3654f6d3.js";import{_ as H}from"./index.2d1a2808.js";import{ah as m,o as O,c as x,V as f,P as h,a as w,U as D,T as J,ar as B,Q as M}from"./vendor-vue.cefe3aef.js";import{h as T}from"./highlight-util.a4f1867f.js";import"./element-plus.af689926.js";import"./element-icon.1fe9d2a8.js";import"./vendor-lib.a8c0b8df.js";const F={name:"",components:{},props:{list:{type:Array}},computed:{},data(){return{currentRow:null,dialogVisible:!1}},methods:{handleEditRow(n){this.currentRow=n,this.dialogVisible=!0},async handleDeleteClick(n){let e={id:n.id};const t=await this.$http.function(e);t.code==0?(this.$msg.success("\u64CD\u4F5C\u6210\u529F"),this.$emit("on-success")):this.$msg.error(t.msg)},async handleStatusChange(n){let e={id:n.id};const t=await this.$http.function(e);t.code==0?(this.$msg.success("\u64CD\u4F5C\u6210\u529F"),this.$emit("on-success")):this.$msg.error(t.msg)},handleUpdateSuccess(){this.$emit("on-success")}},mounted(){U.highlightAll()},created(){}},W={key:0},Q=["innerHTML"],Z={key:1},G=["innerHTML"];function X(n,e,t,s,r,o){const a=m("el-table-column"),u=m("el-tag"),l=m("el-table");return O(),x("div",null,[f(l,{data:t.list,stripe:"",border:""},{default:h(()=>[f(a,{label:n.$t("\u64CD\u4F5C\u4EBA"),"header-align":"center",align:"center",width:"100",prop:"user_name","show-overflow-tooltip":""},{default:h(i=>[w("span",null,D(i.row.user_name||"-"),1)]),_:1},8,["label"]),f(a,{label:n.$t("\u64CD\u4F5C\u8868"),width:"120","header-align":"center",align:"center",prop:"table","show-overflow-tooltip":""},{default:h(i=>[w("span",null,D(i.row.table||"-"),1)]),_:1},8,["label"]),f(a,{label:n.$t("\u64CD\u4F5C\u7C7B\u578B"),"header-align":"center",align:"center",prop:"type_id",width:"100"},{default:h(i=>[f(u,{type:i.row.type_style},{default:h(()=>[J(D(i.row.type_label),1)]),_:2},1032,["type"])]),_:1},8,["label"]),f(a,{label:n.$t("\u6570\u636E\u53D8\u5316"),"header-align":"center",align:"left",prop:"type_id"},{default:h(i=>[i.row.type_style==""?(O(),x("pre",W,[w("code",{class:"language-diff",innerHTML:i.row.data},null,8,Q)])):(O(),x("pre",Z,[w("code",{class:"language-json",innerHTML:i.row.data},null,8,G)]))]),_:1},8,["label"]),f(a,{label:n.$t("\u64CD\u4F5C\u65F6\u95F4"),"header-align":"center",align:"center",prop:"create_time",width:"130"},{default:h(i=>[w("span",null,D(i.row.create_time_label||"-"),1)]),_:1},8,["label"])]),_:1},8,["data"])])}const Y=H(F,[["render",X]]),b={CREATE:1,UPDATE:2,DELETE:3,BATCH_DELETE:4};function v(){}v.prototype={diff:function(e,t){var s=arguments.length>2&&arguments[2]!==void 0?arguments[2]:{},r=s.callback;typeof s=="function"&&(r=s,s={}),this.options=s;var o=this;function a(c){return r?(setTimeout(function(){r(void 0,c)},0),!0):c}e=this.castInput(e),t=this.castInput(t),e=this.removeEmpty(this.tokenize(e)),t=this.removeEmpty(this.tokenize(t));var u=t.length,l=e.length,i=1,d=u+l;s.maxEditLength&&(d=Math.min(d,s.maxEditLength));var p=[{newPos:-1,components:[]}],g=this.extractCommon(p[0],t,e,0);if(p[0].newPos+1>=u&&g+1>=l)return a([{value:this.join(t),count:t.length}]);function _(){for(var c=-1*i;c<=i;c+=2){var y=void 0,C=p[c-1],z=p[c+1],$=(z?z.newPos:0)-c;C&&(p[c-1]=void 0);var k=C&&C.newPos+1<u,V=z&&0<=$&&$<l;if(!k&&!V){p[c]=void 0;continue}if(!k||V&&C.newPos<z.newPos?(y=K(z),o.pushComponent(y.components,void 0,!0)):(y=C,y.newPos++,o.pushComponent(y.components,!0,void 0)),$=o.extractCommon(y,t,e,c),y.newPos+1>=u&&$+1>=l)return a(P(o,y.components,t,e,o.useLongestToken));p[c]=y}i++}if(r)(function c(){setTimeout(function(){if(i>d)return r();_()||c()},0)})();else for(;i<=d;){var L=_();if(L)return L}},pushComponent:function(e,t,s){var r=e[e.length-1];r&&r.added===t&&r.removed===s?e[e.length-1]={count:r.count+1,added:t,removed:s}:e.push({count:1,added:t,removed:s})},extractCommon:function(e,t,s,r){for(var o=t.length,a=s.length,u=e.newPos,l=u-r,i=0;u+1<o&&l+1<a&&this.equals(t[u+1],s[l+1]);)u++,l++,i++;return i&&e.components.push({count:i}),e.newPos=u,l},equals:function(e,t){return this.options.comparator?this.options.comparator(e,t):e===t||this.options.ignoreCase&&e.toLowerCase()===t.toLowerCase()},removeEmpty:function(e){for(var t=[],s=0;s<e.length;s++)e[s]&&t.push(e[s]);return t},castInput:function(e){return e},tokenize:function(e){return e.split("")},join:function(e){return e.join("")}};function P(n,e,t,s,r){for(var o=0,a=e.length,u=0,l=0;o<a;o++){var i=e[o];if(i.removed){if(i.value=n.join(s.slice(l,l+i.count)),l+=i.count,o&&e[o-1].added){var p=e[o-1];e[o-1]=e[o],e[o]=p}}else{if(!i.added&&r){var d=t.slice(u,u+i.count);d=d.map(function(_,L){var c=s[l+L];return c.length>_.length?c:_}),i.value=n.join(d)}else i.value=n.join(t.slice(u,u+i.count));u+=i.count,i.added||(l+=i.count)}}var g=e[a-1];return a>1&&typeof g.value=="string"&&(g.added||g.removed)&&n.equals("",g.value)&&(e[a-2].value+=g.value,e.pop()),e}function K(n){return{newPos:n.newPos,components:n.components.slice(0)}}var I=/^[A-Za-z\xC0-\u02C6\u02C8-\u02D7\u02DE-\u02FF\u1E00-\u1EFF]+$/,R=/\S/,q=new v;q.equals=function(n,e){return this.options.ignoreCase&&(n=n.toLowerCase(),e=e.toLowerCase()),n===e||this.options.ignoreWhitespace&&!R.test(n)&&!R.test(e)};q.tokenize=function(n){for(var e=n.split(/([^\S\r\n]+|[()[\]{}'"\r\n]|\b)/),t=0;t<e.length-1;t++)!e[t+1]&&e[t+2]&&I.test(e[t])&&I.test(e[t+2])&&(e[t]+=e[t+2],e.splice(t+1,2),t--);return e};var j=new v;j.tokenize=function(n){var e=[],t=n.split(/(\n|\r\n)/);t[t.length-1]||t.pop();for(var s=0;s<t.length;s++){var r=t[s];s%2&&!this.options.newlineIsToken?e[e.length-1]+=r:(this.options.ignoreWhitespace&&(r=r.trim()),e.push(r))}return e};var ee=new v;ee.tokenize=function(n){return n.split(/(\S.+?[.!?])(?=\s+|$)/)};var te=new v;te.tokenize=function(n){return n.split(/([{}:;,]|\s+)/)};function A(n){return typeof Symbol=="function"&&typeof Symbol.iterator=="symbol"?A=function(e){return typeof e}:A=function(e){return e&&typeof Symbol=="function"&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},A(n)}var ne=Object.prototype.toString,E=new v;E.useLongestToken=!0;E.tokenize=j.tokenize;E.castInput=function(n){var e=this.options,t=e.undefinedReplacement,s=e.stringifyReplacer,r=s===void 0?function(o,a){return typeof a>"u"?t:a}:s;return typeof n=="string"?n:JSON.stringify(S(n,null,null,r),r,"  ")};E.equals=function(n,e){return v.prototype.equals.call(E,n.replace(/,([\r\n])/g,"$1"),e.replace(/,([\r\n])/g,"$1"))};function S(n,e,t,s,r){e=e||[],t=t||[],s&&(n=s(r,n));var o;for(o=0;o<e.length;o+=1)if(e[o]===n)return t[o];var a;if(ne.call(n)==="[object Array]"){for(e.push(n),a=new Array(n.length),t.push(a),o=0;o<n.length;o+=1)a[o]=S(n[o],e,t,s,r);return e.pop(),t.pop(),a}if(n&&n.toJSON&&(n=n.toJSON()),A(n)==="object"&&n!==null){e.push(n),a={},t.push(a);var u=[],l;for(l in n)n.hasOwnProperty(l)&&u.push(l);for(u.sort(),o=0;o<u.length;o+=1)l=u[o],a[l]=S(n[l],e,t,s,l);e.pop(),t.pop()}else a=n;return a}var N=new v;N.tokenize=function(n){return n.slice()};N.join=N.removeEmpty=function(n){return n};function oe(n,e,t){return N.diff(n,e,t)}const se={name:"log_operation-list",props:{},components:{DataTable:Y},data(){return{list:[],total:0,page:1,size:20,keyword:"",loading:!0,dialogVisible:!1,pageSizeCachekey:"pageSize"}},computed:{},methods:{resetData(){this.page=1,this.list=[],this.getData()},async getData(){this.loading=!0;let n={page:this.page,size:this.size,keyword:this.keyword};try{const e=await this.$http.getOperationLogList(n);e.code==0&&(this.list=e.data.list.map(t=>{try{t.before=JSON.stringify(JSON.parse(t.before),null,2)}catch{}try{t.after=JSON.stringify(JSON.parse(t.after),null,2)}catch{}if(t.type_id==b.UPDATE){let r=oe(t.before.split(`
`),t.after.split(`
`)).map(o=>o.added?o.value.map(a=>"+"+a).join(`
`):o.removed?o.value.map(a=>"-"+a).join(`
`):o.value.map(a=>a).join(`
`));t.data=T(r.join(`
`),{language:"diff"}).value,t.type_style=""}else t.type_id==b.CREATE?(t.data=T(t.after,{language:"json"}).value,t.type_style="success"):t.type_id==b.DELETE?(t.data=T(t.before,{language:"json"}).value,t.type_style="danger"):t.type_id==b.BATCH_DELETE&&(t.data=T(t.before,{language:"json"}).value,t.type_style="danger");return t}),this.total=e.data.total)}catch(e){console.log(e)}finally{this.loading=!1}},handleAddRow(){this.dialogVisible=!0},handleAddSuccess(){this.resetData()},getObjectString(n){let e=[];for(let[t,s]of Object.entries(n))e.push(`${t}: ${s}`);return e.join(`
`)},handleSearch(){this.resetData()},handleSizeChange(n){localStorage.setItem(this.pageSizeCachekey,n),this.resetData()},loadPageSize(){let n=localStorage.getItem(this.pageSizeCachekey);n&&(this.size=parseInt(n))},async clearLogOperationList(){let n=this.$loading({fullscreen:!0});try{const e=await this.$http.clearLogOperationList();e.code==0?(this.$msg.success("\u64CD\u4F5C\u6210\u529F"),this.resetData()):this.$msg.error(e.msg)}catch(e){console.log(e)}finally{this.$nextTick(()=>{n.close()})}}},created(){this.loadPageSize(),this.getData()}},ie={class:"app-container"},re={class:"flex justify-between mb-sm"},ae=w("div",null,null,-1);function le(n,e,t,s,r,o){const a=m("Delete"),u=m("el-icon"),l=m("el-link"),i=m("el-popconfirm"),d=m("DataTable"),p=m("el-pagination"),g=B("loading");return O(),x("div",ie,[w("div",re,[ae,f(i,{title:"\u786E\u5B9A\u6E05\u7A7A\u65E5\u5FD7\uFF1F",onConfirm:o.clearLogOperationList},{reference:h(()=>[f(l,{underline:!1,type:"danger",class:"mr-sm"},{default:h(()=>[f(u,null,{default:h(()=>[f(a)]),_:1}),J(D(n.$t("\u6E05\u7A7A\u65E5\u5FD7")),1)]),_:1})]),_:1},8,["onConfirm"])]),M(f(d,{list:r.list,onOnSuccess:o.resetData},null,8,["list","onOnSuccess"]),[[g,r.loading]]),f(p,{class:"mt-md justify-center",background:"",layout:"total, sizes, prev, pager, next",total:r.total,"page-size":r.size,"onUpdate:pageSize":e[0]||(e[0]=_=>r.size=_),"current-page":r.page,"onUpdate:currentPage":e[1]||(e[1]=_=>r.page=_),onCurrentChange:o.getData,onSizeChange:o.handleSizeChange},null,8,["total","page-size","current-page","onCurrentChange","onSizeChange"])])}const _e=H(se,[["render",le]]);export{_e as default};

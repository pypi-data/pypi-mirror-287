import{c as H}from"./element-plus.af689926.js";import{c as P}from"./commonjs-dynamic-modules.cee4dbcc.js";import{_ as w}from"./index.2d1a2808.js";import{o as h,c as V,I as E,a as m,J as q,U as C,F as R,a8 as T,K as D,ah as v,O as U,P as S,V as p}from"./vendor-vue.cefe3aef.js";import{i as G}from"./index.afa609c1.js";import"./element-icon.1fe9d2a8.js";import"./vendor-lib.a8c0b8df.js";var N={exports:{}};(function(e,o){(function(n,i){e.exports=i(P,o,e)})(H,function(n,i,d){var a=function(l,f,g,I,M,y){for(var k=0,A=["webkit","moz","ms","o"],$=0;$<A.length&&!window.requestAnimationFrame;++$)window.requestAnimationFrame=window[A[$]+"RequestAnimationFrame"],window.cancelAnimationFrame=window[A[$]+"CancelAnimationFrame"]||window[A[$]+"CancelRequestAnimationFrame"];window.requestAnimationFrame||(window.requestAnimationFrame=function(r,s){var u=new Date().getTime(),_=Math.max(0,16-(u-k)),x=window.setTimeout(function(){r(u+_)},_);return k=u+_,x}),window.cancelAnimationFrame||(window.cancelAnimationFrame=function(r){clearTimeout(r)});var t=this;t.options={useEasing:!0,useGrouping:!0,separator:",",decimal:".",easingFn:null,formattingFn:null};for(var F in y)y.hasOwnProperty(F)&&(t.options[F]=y[F]);t.options.separator===""&&(t.options.useGrouping=!1),t.options.prefix||(t.options.prefix=""),t.options.suffix||(t.options.suffix=""),t.d=typeof l=="string"?document.getElementById(l):l,t.startVal=Number(f),t.endVal=Number(g),t.countDown=t.startVal>t.endVal,t.frameVal=t.startVal,t.decimals=Math.max(0,I||0),t.dec=Math.pow(10,t.decimals),t.duration=1e3*Number(M)||2e3,t.formatNumber=function(r){r=r.toFixed(t.decimals),r+="";var s,u,_,x;if(s=r.split("."),u=s[0],_=s.length>1?t.options.decimal+s[1]:"",x=/(\d+)(\d{3})/,t.options.useGrouping)for(;x.test(u);)u=u.replace(x,"$1"+t.options.separator+"$2");return t.options.prefix+u+_+t.options.suffix},t.easeOutExpo=function(r,s,u,_){return u*(-Math.pow(2,-10*r/_)+1)*1024/1023+s},t.easingFn=t.options.easingFn?t.options.easingFn:t.easeOutExpo,t.formattingFn=t.options.formattingFn?t.options.formattingFn:t.formatNumber,t.version=function(){return"1.7.1"},t.printValue=function(r){var s=t.formattingFn(r);t.d.tagName==="INPUT"?this.d.value=s:t.d.tagName==="text"||t.d.tagName==="tspan"?this.d.textContent=s:this.d.innerHTML=s},t.count=function(r){t.startTime||(t.startTime=r),t.timestamp=r;var s=r-t.startTime;t.remaining=t.duration-s,t.options.useEasing?t.countDown?t.frameVal=t.startVal-t.easingFn(s,0,t.startVal-t.endVal,t.duration):t.frameVal=t.easingFn(s,t.startVal,t.endVal-t.startVal,t.duration):t.countDown?t.frameVal=t.startVal-(t.startVal-t.endVal)*(s/t.duration):t.frameVal=t.startVal+(t.endVal-t.startVal)*(s/t.duration),t.countDown?t.frameVal=t.frameVal<t.endVal?t.endVal:t.frameVal:t.frameVal=t.frameVal>t.endVal?t.endVal:t.frameVal,t.frameVal=Math.round(t.frameVal*t.dec)/t.dec,t.printValue(t.frameVal),s<t.duration?t.rAF=requestAnimationFrame(t.count):t.callback&&t.callback()},t.start=function(r){return t.callback=r,t.rAF=requestAnimationFrame(t.count),!1},t.pauseResume=function(){t.paused?(t.paused=!1,delete t.startTime,t.duration=t.remaining,t.startVal=t.frameVal,requestAnimationFrame(t.count)):(t.paused=!0,cancelAnimationFrame(t.rAF))},t.reset=function(){t.paused=!1,delete t.startTime,t.startVal=f,cancelAnimationFrame(t.rAF),t.printValue(t.startVal)},t.update=function(r){cancelAnimationFrame(t.rAF),t.paused=!1,delete t.startTime,t.startVal=t.frameVal,t.endVal=Number(r),t.countDown=t.startVal>t.endVal,t.rAF=requestAnimationFrame(t.count)},t.printValue(t.startVal)};return a})})(N,N.exports);const L=N.exports;const z={name:"countTo",props:{init:{type:Number,required:!1,default:0},startVal:{type:Number,required:!1,default:0},end:{type:Number,required:!0},decimals:{type:Number,required:!1,default:0},decimal:{type:String,required:!1,default:"."},duration:{type:Number,required:!1,default:2},delay:{type:Number,required:!1,default:0},uneasing:{type:Boolean,required:!1,default:!1},usegroup:{type:Boolean,required:!1,default:!1},separator:{type:String,required:!1,default:","},simplify:{type:Boolean,required:!1,default:!1},unit:{type:Array,required:!1,default(){return[[3,"K+"],[6,"M+"],[9,"B+"]]}},countClass:{type:String,required:!1,default:""},unitClass:{type:String,required:!1,default:""}},data(){return{counter:null,unitText:""}},computed:{counterId(){return`count_to_${this._uid}`}},watch:{end(e){let o=this.getValue(e);this.counter.update(o)}},mounted(){this.$nextTick(()=>{let e=this.getValue(this.end);this.counter=new L(this.counterId,this.startVal,e,this.decimals,this.duration,{useEasing:!this.uneasing,useGrouping:this.useGroup,separator:this.separator,decimal:this.decimal}),setTimeout(()=>{this.counter.error||this.counter.start()},this.delay)})},methods:{getHandleVal(e,o){return{endVal:parseInt(e/Math.pow(10,this.unit[o-1][0])),unitText:this.unit[o-1][1]}},transformValue(e){let o=this.unit.length,n={endVal:0,unitText:""};if(e<Math.pow(10,this.unit[0][0]))n.endVal=e;else for(let i=1;i<o;i++)e>=Math.pow(10,this.unit[i-1][0])&&e<Math.pow(10,this.unit[i][0])&&(n=this.getHandleVal(e,i));return e>Math.pow(10,this.unit[o-1][0])&&(n=this.getHandleVal(e,o)),n},getValue(e){let o=0;if(this.simplify){let{endVal:n,unitText:i}=this.transformValue(e);this.unitText=i,o=n}else o=e;return o}}},B={class:"count-to-wrapper"},O={class:"content-outer"},Y=["id"];function W(e,o,n,i,d,a){return h(),V("div",B,[E(e.$slots,"left",{},void 0,!0),m("p",O,[m("span",{class:q(["count-to-count-text",n.countClass]),id:a.counterId},C(n.init),11,Y),m("span",{class:q(["count-to-unit-text",n.unitClass])},C(d.unitText),3)]),E(e.$slots,"right",{},void 0,!0)])}const j=w(z,[["render",W],["__scopeId","data-v-84c2e9f0"]]),c={PRIMARY:"#409eff",SUCCESS:"#67c23a",INFO:"#909399",WARNING:"#e6a23c",DANGER:"#f56c6c"};const K={name:"activePlate",components:{CountTo:j},props:{infoList:{type:Array,require:!0}},data(){return{COLORS:c,colors:["#409eff","#409eff","#409eff","#f56c6c","#f56c6c","#f56c6c"]}},methods:{handleClick(e){console.log(e),this.$router.push({path:e.path})}}},J={class:"active-plate-main"},Z={class:"active-list"},Q=["onClick"],X={class:"desc"};function tt(e,o,n,i,d,a){return h(),V("div",J,[m("ul",Z,[(h(!0),V(R,null,T(n.infoList,(l,f)=>(h(),V("li",{class:"item",onClick:g=>a.handleClick(l)},[m("p",{class:"num",style:D({color:l.color})},C(l.count)+" ",5),m("p",X,C(e.$t(l.title)),1)],8,Q))),256))])])}const et=w(K,[["render",tt]]);const nt={props:{title:{type:String,default:"\u6807\u9898"},desc:{type:String,default:"\u63CF\u8FF0"}}},ot={class:"card-main"},at={class:"card-main__header"},rt={class:"card-main__title"},it={class:"card-main__desc"};function st(e,o,n,i,d,a){return h(),V("div",ot,[m("div",at,[m("div",rt,C(e.$t(n.title)),1),m("div",it,C(e.$t(n.desc)),1)]),E(e.$slots,"default")])}const b=w(nt,[["render",st]]),ct={name:"",props:{list:{type:Array,default:()=>[]}},components:{HomeCard:b,ActivePlate:et},data(){return{}},computed:{},methods:{},created(){}};function lt(e,o,n,i,d,a){const l=v("ActivePlate"),f=v("HomeCard");return h(),U(f,{desc:"System",title:"\u7CFB\u7EDF\u6570\u636E"},{default:S(()=>[p(l,{infoList:n.list},null,8,["infoList"])]),_:1})}const ut=w(ct,[["render",lt]]),dt=function(){return document.addEventListener?function(e,o,n){e&&o&&n&&e.addEventListener(o,n,!1)}:function(e,o,n){e&&o&&n&&e.attachEvent("on"+o,n)}}(),mt=function(){return document.removeEventListener?function(e,o,n){e&&o&&e.removeEventListener(o,n,!1)}:function(e,o,n){e&&o&&e.detachEvent("on"+o,n)}}();const ft={props:{value:Array,text:String,subtext:String},data(){return{chartDom:null}},beforeDestroy(){mt(window,"resize",this.resize)},methods:{resize(){this.chartDom&&this.chartDom.resize()},initChart(e){let o={};for(let a of e)o[a.name]=a.selected;let n=!0;e.forEach(a=>{a.value!=0&&(n=!1)});let i=e.map(a=>a.color);n==!0&&(i=["#cccccc","#cccccc"]);let d={color:i,tooltip:{trigger:"item"},legend:{top:"5%",left:"center",selectedMode:!1},series:[{type:"pie",showEmptyCircle:!0,radius:["30%","60%"],center:["50%","54%"],label:{show:!1},emphasis:{},data:e.map(a=>(a.name=this.$t(a.name),a))}]};this.chartDom||(this.chartDom=G(this.$refs.dom)),this.chartDom.setOption(d),e.forEach(a=>{a.selected||this.chartDom.dispatchAction({type:"legendUnSelect",name:a.name})}),dt(window,"resize",this.resize)}}},_t={class:"pie-main",ref:"dom"};function pt(e,o,n,i,d,a){return h(),V("div",_t,null,512)}const ht=w(ft,[["render",pt]]);const Vt={name:"Home",components:{HomeDataInfo:ut,HomeCard:b,HomeChartPie:ht},props:{},data(){return{virtual_memory:{},disk_usage:{},adModal:!0,list:[],certValue:[],timer:null,systemData:[{title:"\u8BC1\u4E66\u6570\u91CF",key:"ssl_cert_count",count:0,color:c.PRIMARY,path:"/cert/list"},{title:"\u57DF\u540D\u6570\u91CF",key:"domain_count",count:0,path:"/domain/list",color:c.PRIMARY},{title:"\u7F51\u7AD9\u6570\u91CF",key:"monitor_count",path:"/monitor/list",count:0,color:c.PRIMARY},{title:"\u8FC7\u671F\u8BC1\u4E66",key:"ssl_cert_expire_count",count:0,path:"/cert/list",color:c.SUCCESS},{title:"\u8FC7\u671F\u57DF\u540D",key:"domain_expire_count",count:0,path:"/domain/list",color:c.SUCCESS},{title:"\u7F51\u7AD9\u5F02\u5E38",key:"monitor_error_count",count:0,path:"/monitor/list",color:c.SUCCESS}]}},computed:{},watch:{},filters:{},methods:{async getData(){const e=await this.$http.getSystemData();let o={};e.data.forEach(n=>{o[n.key]=n}),console.log(o),this.systemData.forEach(n=>{n.count=o[n.key].count,n.color!=c.PRIMARY&&(n.count>0?n.color=c.DANGER:n.color=c.SUCCESS)}),this.handleInit(o)},handleCertData(e){let n=[{value:e.ssl_cert_count.count-e.ssl_cert_expire_count.count-e.ssl_cert_will_expire_count.count,name:"\u672A\u8FC7\u671F",color:c.SUCCESS,selected:e.ssl_cert_count.count>0},{value:e.ssl_cert_will_expire_count.count,name:"\u5373\u5C06\u8FC7\u671F",color:c.WARNING,selected:e.ssl_cert_count.count>0},{value:e.ssl_cert_expire_count.count,name:"\u5DF2\u8FC7\u671F",color:c.DANGER,selected:e.ssl_cert_count.count>0}];this.$refs.HomeChartCertPie.initChart(n)},handleDomainData(e){let n=[{value:e.domain_count.count-e.domain_will_expire_count.count-e.domain_expire_count.count,name:"\u672A\u8FC7\u671F",color:c.SUCCESS,selected:e.domain_count.count>0},{value:e.domain_will_expire_count.count,name:"\u5373\u5C06\u8FC7\u671F",color:c.WARNING,selected:e.domain_count.count>0},{value:e.domain_expire_count.count,name:"\u5DF2\u8FC7\u671F",color:c.DANGER,selected:e.domain_count.count>0}];this.$refs.HomeChartDomainPie.initChart(n)},handleMonitorData(e){let n=[{value:e.monitor_count.count-e.monitor_error_count.count,name:"\u6B63\u5E38",color:c.SUCCESS,selected:e.monitor_count.count>0},{value:e.monitor_error_count.count,name:"\u5F02\u5E38",color:c.DANGER,selected:e.monitor_count.count>0}];this.$refs.HomeChartMonitorPie.initChart(n)},handleInit(e){console.log(e),this.handleCertData(e),this.handleDomainData(e),this.handleMonitorData(e)}},beforeUnmount(){console.log("beforeUnmount"),this.timer&&(clearInterval(this.timer),this.timer=null)},mounted(){console.log("mounted"),this.timer=setInterval(()=>{this.getData()},1e3*60*1),this.getData()}},gt={class:"app-container dashboard"},Ct={class:"grid mt-md gap-[20px] grid-cols-3"};function wt(e,o,n,i,d,a){const l=v("HomeDataInfo"),f=v("HomeChartPie"),g=v("HomeCard");return h(),V("div",gt,[p(l,{list:d.systemData},null,8,["list"]),m("div",Ct,[p(g,{title:"\u8BC1\u4E66\u7EDF\u8BA1",desc:"SSL Cert"},{default:S(()=>[p(f,{ref:"HomeChartCertPie"},null,512)]),_:1}),p(g,{title:"\u57DF\u540D\u7EDF\u8BA1",desc:"Domain"},{default:S(()=>[p(f,{ref:"HomeChartDomainPie"},null,512)]),_:1}),p(g,{title:"\u76D1\u63A7\u7EDF\u8BA1",desc:"Monitor"},{default:S(()=>[p(f,{ref:"HomeChartMonitorPie"},null,512)]),_:1})])])}const Et=w(Vt,[["render",wt]]);export{Et as default};

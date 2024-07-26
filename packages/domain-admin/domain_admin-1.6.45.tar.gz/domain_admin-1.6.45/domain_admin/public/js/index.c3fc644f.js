import{i as X}from"./validator-util.99457e19.js";import{S as N}from"./SelectGroup.91835d0e.js";import{_ as S,R as L,d as G,r as J}from"./index.2d1a2808.js";import{ah as a,ar as T,Q as A,o as u,c as g,V as o,P as n,a as c,F as O,a8 as Z,O as v,T as D,U as _,S as C,L as ee,ax as q,ay as te,a9 as oe}from"./vendor-vue.cefe3aef.js";import{E as j,A as le,a as ie}from"./DataTableDialog.db44056c.js";import{C as ne}from"./ConnectStatus.4db38fcf.js";import{E as ae}from"./ExpireProgress.a15419ca.js";import{F as se}from"./vendor-lib.a8c0b8df.js";import{u as P}from"./group-store.7cabd898.js";import{E as re}from"./event-enums.f8a2c250.js";import{C as de,E as me}from"./ExportFileDialog.f3781bf6.js";import{D as ue}from"./DataCount.72aeb599.js";import{d as ce}from"./element-plus.af689926.js";import"./element-icon.1fe9d2a8.js";const pe=[{label:"SSL/TLS",value:0},{label:"STARTTLS",value:1}],_e={domain:[{message:"\u57DF\u540D\u4E0D\u80FD\u4E3A\u7A7A",required:!0,trigger:"blur"}],port:[{required:!0,trigger:"blur",validator:(e,t,l)=>{if(!t)return l();if(X(t))l();else return l(new Error("\u7AEF\u53E3\u53F7\u53EA\u80FD\u662F\u6570\u5B57"))}}]},he={name:"",props:{row:{type:Object,default:null}},components:{SelectGroup:N},data(){return{sslTypeOptions:pe,loading:!1,form:{domain:"",alias:"",port:443,group_id:"",is_dynamic_host:!1,ssl_type:0,start_time:"",expire_time:"",auto_update:!0},rules:_e}},computed:{disabledDomain(){return!!this.row}},methods:{async getData(){if(this.loading=!0,this.row){let e={id:this.row.id},l=(await this.$http.getDomainById(e)).data;this.form.domain=l.domain,this.form.alias=l.alias,this.form.group_id=l.group_id,this.form.port=l.port,this.form.ssl_type=l.ssl_type,this.form.start_time=l.start_time,this.form.expire_time=l.expire_time,this.form.auto_update=l.auto_update,this.form.group_id==0&&(this.form.group_id="")}this.loading=!1},handleCancel(){this.$emit("on-cancel")},handleSubmit(){console.log("handleSubmit",this.form),this.$refs.form.validate(e=>{if(console.log(e),e)this.confirmSubmit();else return!1})},async confirmSubmit(){let e=this.$loading({fullscreen:!0}),t={domain:this.form.domain.trim(),alias:this.form.alias.trim(),group_id:this.form.group_id,port:this.form.port,ssl_type:this.form.ssl_type,start_time:this.form.start_time,expire_time:this.form.expire_time,auto_update:this.form.auto_update},l=null;this.row?(t.id=this.row.id,l=await this.$http.updateDomainById(t)):l=await this.$http.addDomain(t),l.ok&&(this.$msg.success("\u64CD\u4F5C\u6210\u529F"),this.$emit("on-success")),this.$nextTick(()=>{e.close()})},async handleDomainChange(){}},created(){this.getData()}},fe={class:"flex"},ge={class:"flex justify-between w-full"},be=c("span",null," - ",-1),we={class:"grid grid-cols-2"},ye={class:"text-center"};function De(e,t,l,h,i,s){const m=a("el-input"),d=a("el-form-item"),p=a("el-date-picker"),V=a("el-switch"),y=a("Warning"),b=a("el-icon"),R=a("el-link"),U=a("el-tooltip"),x=a("el-option"),$=a("el-select"),I=a("SelectGroup"),E=a("el-form"),F=a("el-button"),B=T("loading");return A((u(),g("div",null,[o(E,{ref:"form",model:i.form,rules:i.rules,"label-width":"100px"},{default:n(()=>[c("div",fe,[o(d,{label:e.$t("\u57DF\u540D"),prop:"domain",class:"flex-1"},{default:n(()=>[o(m,{type:"text",modelValue:i.form.domain,"onUpdate:modelValue":t[0]||(t[0]=f=>i.form.domain=f),placeholder:e.$t("\u8BF7\u8F93\u5165\u57DF\u540D"),onBlur:s.handleDomainChange},null,8,["modelValue","placeholder","onBlur"])]),_:1},8,["label"]),o(d,{label:e.$t("\u7AEF\u53E3"),prop:"port",style:{width:"160px"}},{default:n(()=>[o(m,{type:"text",modelValue:i.form.port,"onUpdate:modelValue":t[1]||(t[1]=f=>i.form.port=f),placeholder:e.$t("\u8BF7\u8F93\u5165\u7AEF\u53E3")},null,8,["modelValue","placeholder"])]),_:1},8,["label"])]),o(d,{label:e.$t("\u8BC1\u4E66\u65F6\u95F4"),prop:"start_time"},{default:n(()=>[c("div",ge,[o(p,{modelValue:i.form.start_time,"onUpdate:modelValue":t[2]||(t[2]=f=>i.form.start_time=f),type:"date","value-format":"YYYY-MM-DD HH:mm:ss",placeholder:e.$t("\u8BC1\u4E66\u9881\u53D1\u65F6\u95F4"),disabled:i.form.auto_update,style:{width:"180px"}},null,8,["modelValue","placeholder","disabled"]),be,o(p,{modelValue:i.form.expire_time,"onUpdate:modelValue":t[3]||(t[3]=f=>i.form.expire_time=f),type:"date","value-format":"YYYY-MM-DD HH:mm:ss",placeholder:e.$t("\u8BC1\u4E66\u8FC7\u671F\u65F6\u95F4"),disabled:i.form.auto_update,style:{width:"180px"}},null,8,["modelValue","placeholder","disabled"])])]),_:1},8,["label"]),c("div",we,[o(d,{label:e.$t("\u81EA\u52A8\u66F4\u65B0"),prop:"auto_update"},{default:n(()=>[o(V,{modelValue:i.form.auto_update,"onUpdate:modelValue":t[4]||(t[4]=f=>i.form.auto_update=f)},null,8,["modelValue"]),o(U,{effect:"dark",content:"\u5982\u9700\u624B\u52A8\u8BBE\u7F6E\u8BC1\u4E66\u65F6\u95F4\uFF0C\u9700\u5173\u95ED\u81EA\u52A8\u66F4\u65B0",placement:"top-start","show-after":500},{default:n(()=>[o(R,{underline:!1},{default:n(()=>[o(b,{class:"ml-sm"},{default:n(()=>[o(y)]),_:1})]),_:1})]),_:1})]),_:1},8,["label"]),o(d,{label:e.$t("\u52A0\u5BC6\u65B9\u5F0F"),prop:"ssl_type"},{default:n(()=>[o($,{modelValue:i.form.ssl_type,"onUpdate:modelValue":t[5]||(t[5]=f=>i.form.ssl_type=f),placeholder:e.$t("\u52A0\u5BC6\u65B9\u5F0F")},{default:n(()=>[(u(!0),g(O,null,Z(i.sslTypeOptions,f=>(u(),v(x,{key:f.value,label:f.label,value:f.value},null,8,["label","value"]))),128))]),_:1},8,["modelValue","placeholder"])]),_:1},8,["label"])]),o(d,{label:e.$t("\u5206\u7EC4"),prop:"group_id"},{default:n(()=>[o(I,{class:"w-[150px]",modelValue:i.form.group_id,"onUpdate:modelValue":t[6]||(t[6]=f=>i.form.group_id=f),clearable:""},null,8,["modelValue"])]),_:1},8,["label"]),o(d,{label:e.$t("\u5907\u6CE8"),prop:"alias"},{default:n(()=>[o(m,{type:"textarea",modelValue:i.form.alias,"onUpdate:modelValue":t[7]||(t[7]=f=>i.form.alias=f),rows:3,placeholder:e.$t("\u8BF7\u8F93\u5165\u5907\u6CE8")},null,8,["modelValue","placeholder"])]),_:1},8,["label"])]),_:1},8,["model","rules"]),c("div",ye,[o(F,{onClick:s.handleCancel},{default:n(()=>[D(_(e.$t("\u53D6\u6D88")),1)]),_:1},8,["onClick"]),o(F,{type:"primary",onClick:s.handleSubmit},{default:n(()=>[D(_(e.$t("\u786E\u5B9A")),1)]),_:1},8,["onClick"])])])),[[B,i.loading]])}const Ce=S(he,[["render",De]]),ke={name:"",props:{row:{type:Object,default:null},visible:{type:Boolean,default:!1}},emits:["update:visible"],components:{DataForm:Ce},data(){return{}},computed:{dialogTitle(){return this.row?this.$t("\u7F16\u8F91\u57DF\u540D"):this.$t("\u6DFB\u52A0\u57DF\u540D")},dialogVisible:{get(){return this.visible},set(e){this.$emit("update:visible",e)}}},methods:{handleClose(){this.dialogVisible=!1},handleOpen(){this.dialogVisible=!0},handleSuccess(){this.handleClose(),this.$emit("on-success")}},created(){}};function ve(e,t,l,h,i,s){const m=a("DataForm"),d=a("el-dialog");return u(),v(d,{title:s.dialogTitle,modelValue:s.dialogVisible,"onUpdate:modelValue":t[0]||(t[0]=p=>s.dialogVisible=p),width:"530px",center:"","append-to-body":"","lock-scroll":!1},{default:n(()=>[s.dialogVisible?(u(),v(m,{key:0,row:l.row,onOnCancel:s.handleClose,onOnSuccess:s.handleSuccess},null,8,["row","onOnCancel","onOnSuccess"])):C("",!0)]),_:1},8,["title","modelValue"])}const H=S(ke,[["render",ve]]),Ve={name:"",props:{row:{type:Object,default:null}},components:{ExpireDays:j,AddressList:le},data(){return{form:{domain:"",domain_url:"",ip:"",start_time:"",expire_time:"",check_time:"",connect_status:"",total_days:"",expire_days:"",create_time:"",update_time:"",group_name:"",real_time_expire_days:"",domain_start_time:"",domain_expire_time:"",real_time_domain_expire_days:"",alias:"",domain_auto_update:"",domain_auto_update_label:"",domain_expire_monitor:"",domain_check_time_label:"",port:"",address_count:0,group:null},ipInfo:{isp:""}}},computed:{},methods:{async getData(){if(this.row){let e={id:this.row.id};const t=await this.$http.getDomainById(e);if(!t.ok)return;let l=t.data;this.form.domain=l.domain,this.form.domain_url=l.domain_url,this.form.ip=l.ip,this.form.start_time=l.start_time,this.form.expire_time=l.expire_time,this.form.check_time=l.check_time,this.form.connect_status=l.connect_status,this.form.total_days=l.total_days,this.form.expire_days=l.expire_days,this.form.real_time_expire_days=l.real_time_expire_days,this.form.create_time=l.create_time,this.form.update_time_label=l.update_time_label,this.form.domain_auto_update=l.domain_auto_update,this.form.domain_auto_update_label=l.domain_auto_update==!0?"\u662F":"\u5426",this.form.domain_expire_monitor=l.domain_expire_monitor==!0?"\u662F":"\u5426",this.form.domain_check_time_label=l.domain_check_time_label,this.form.port=l.port,this.form.alias=l.alias,this.form.domain_start_time=l.domain_start_time,this.form.domain_expire_time=l.domain_expire_time,this.form.real_time_domain_expire_days=l.real_time_domain_expire_days,this.form.address_count=l.address_count,this.form.group=l.group,this.form.group_name=l.group_name}},handleCancel(){this.$emit("on-cancel")},async handleUpdateRowDomainInfo(){let e=this.$loading({lock:!0,text:"\u66F4\u65B0\u4E2D"}),t={domain_id:this.row.id};(await this.$http.updateDomainCertInfoById(t)).code==0&&(this.$msg.success("\u64CD\u4F5C\u6210\u529F"),this.getData()),e.close()},async getIpInfo(){let e={ip:this.form.ip};const t=await this.$http.getIpInfo(e);t.code==0&&(this.ipInfo=t.data)}},created(){this.getData()}},Se={class:"domain-detail"},xe={class:"mo-form-detail grid grid-cols-2"},Re={key:0},Ue={key:1},Fe={class:"flex justify-between flex-1"},Oe={class:"truncate"},$e={class:"mo-form-detail mt-[20px]"},Ie={class:"truncate"},Ee={class:"text-center mt-md"};function Be(e,t,l,h,i,s){const m=a("el-link"),d=a("el-form-item"),p=a("el-form"),V=a("ExpireDays"),y=a("Refresh"),b=a("el-icon"),R=a("el-button");return u(),g("div",Se,[c("div",xe,[o(p,{"label-width":"130px"},{default:n(()=>[o(d,{label:"\u57DF\u540D",prop:"domain"},{default:n(()=>[o(m,{underline:!1,href:i.form.domain_url,target:"_blank"},{default:n(()=>[D(_(i.form.domain),1)]),_:1},8,["href"])]),_:1}),o(d,{label:"\u8BC1\u4E66\u9881\u53D1\u65F6\u95F4",prop:"create_time"},{default:n(()=>[c("span",null,_(i.form.start_time||"-"),1)]),_:1}),o(d,{label:"\u8BC1\u4E66\u8FC7\u671F\u65F6\u95F4",prop:"create_time"},{default:n(()=>[c("span",null,_(i.form.expire_time||"-"),1)]),_:1}),o(d,{label:"\u5206\u7EC4",prop:"create_time"},{default:n(()=>[i.form.group_name?(u(),g("span",Re,_(i.form.group_name||"-"),1)):(u(),g("span",Ue,"-"))]),_:1})]),_:1}),o(p,{"label-width":"130px",style:{"margin-right":"-1px"}},{default:n(()=>[o(d,{label:"\u7AEF\u53E3\u53F7",prop:"domain"},{default:n(()=>[c("span",null,_(i.form.port||"-"),1)]),_:1}),o(d,{label:"\u5269\u4F59\u5929\u6570",prop:"create_time"},{default:n(()=>[o(V,{value:i.form.real_time_expire_days},null,8,["value"])]),_:1}),o(d,{label:"\u68C0\u67E5\u65F6\u95F4",prop:"isp"},{default:n(()=>[c("div",Fe,[c("span",Oe,_(i.form.update_time_label||"-"),1),o(m,{underline:!1,type:"primary",class:"mr-sm",onClick:s.handleUpdateRowDomainInfo},{default:n(()=>[o(b,null,{default:n(()=>[o(y)]),_:1})]),_:1},8,["onClick"])])]),_:1}),o(d,{label:"\u4E3B\u673A\u6570\u91CF",prop:"create_time"},{default:n(()=>[c("span",null,_(i.form.address_count||"-"),1)]),_:1})]),_:1})]),c("div",$e,[o(p,{"label-width":"130px"},{default:n(()=>[o(d,{label:"\u5907\u6CE8",prop:"isp"},{default:n(()=>[c("span",Ie,_(i.form.alias||"-"),1)]),_:1})]),_:1})]),c("div",Ee,[o(R,{type:"primary",onClick:s.handleCancel},{default:n(()=>[D("\u5173 \u95ED")]),_:1},8,["onClick"])])])}const Te=S(Ve,[["render",Be]]),Ae={name:"",props:{row:{type:Object,default:null},visible:{type:Boolean,default:!1}},emits:["update:visible"],components:{DataForm:Te},data(){return{}},computed:{dialogTitle(){return this.row?"\u7F16\u8F91":"\u6DFB\u52A0"},dialogVisible:{get(){return this.visible},set(e){this.$emit("update:visible",e)}}},methods:{handleClose(){this.dialogVisible=!1},handleOpen(){this.dialogVisible=!0},handleSuccess(){this.handleClose()},handleDialogClose(){this.$emit("on-success")}},created(){}};function ze(e,t,l,h,i,s){const m=a("DataForm"),d=a("el-dialog");return u(),v(d,{title:"\u8BC1\u4E66\u8BE6\u60C5",modelValue:s.dialogVisible,"onUpdate:modelValue":t[0]||(t[0]=p=>s.dialogVisible=p),width:"800px",center:"","append-to-body":"","lock-scroll":!1,onClose:s.handleDialogClose},{default:n(()=>[s.dialogVisible?(u(),v(m,{key:0,row:l.row,onOnCancel:s.handleClose,onOnSuccess:s.handleSuccess},null,8,["row","onOnCancel","onOnSuccess"])):C("",!0)]),_:1},8,["modelValue","onClose"])}const Le=S(Ae,[["render",ze]]),Pe={name:"",components:{DataFormDialog:H,DataDetailDialog:Le,ConnectStatus:ne,ExpireDays:j,ExpireProgress:ae,AddressListgDialog:ie},emits:["on-success","selection-change","sort-change","on-refresh-row"],props:{role:{type:Number}},computed:{},data(){return{RoleEnum:L,currentRow:null,dialogVisible:!1,dialogDetailVisible:!1,AddressListgDialogVisible:!1}},methods:{handleEditRow(e){this.currentRow=e,this.dialogVisible=!0},async handleDeleteClick(e){let t={id:e.id};const l=await this.$http.deleteDomainById(t);l.code==0?(this.$msg.success("\u64CD\u4F5C\u6210\u529F"),this.$emit("on-success")):this.$msg.error(l.msg)},async handleStatusChange(e){let t={id:e.id};const l=await this.$Http.function(t);l.code==0?(this.$msg.success("\u64CD\u4F5C\u6210\u529F"),this.$emit("on-success")):this.$msg.error(l.msg)},async handleMonitorStatusChange(e,t){let l={domain_id:e.id,is_monitor:t};const h=await this.$http.updateDomainExpireMonitorById(l);h.code==0?this.$msg.success("\u64CD\u4F5C\u6210\u529F"):this.$msg.error(h.msg)},async handleUpdateRowDomainInfo(e){let t=this.$loading({lock:!0,text:"\u66F4\u65B0\u4E2D"}),l={id:e.id};(await this.$http.updateDomainRowInfoById(l)).code==0&&(this.$msg.success("\u64CD\u4F5C\u6210\u529F"),this.$emit("on-success")),t.close()},handleUpdateSuccess(){this.$emit("on-success")},handleDetailSuccess(){},handleShowDetail(e){this.currentRow=e,this.dialogDetailVisible=!0},handleShowAddressListgDialog(e){this.currentRow=e,this.AddressListgDialogVisible=!0},async handleAutoUpdateStatusChange(e,t){let l={domain_id:e.id,field:"auto_update",value:t};const h=await this.$http.updateDomainFieldById(l);h.code==0?this.$msg.success("\u64CD\u4F5C\u6210\u529F"):this.$msg.error(h.msg)},handleRefreshRow(e){this.$emit("on-refresh-row",e)},handleSelectable(e,t){return e.has_edit_permission}},created(){}},Ge={class:"inline-flex items-center"},Ne={class:"mr-[2px]"},qe={key:0},je={key:0,class:"color--danger"},He={class:"inline-flex items-center"},Ye={class:"mr-[2px]"};function Me(e,t,l,h,i,s){const m=a("el-table-column"),d=a("Warning"),p=a("el-icon"),V=a("el-tooltip"),y=a("el-link"),b=a("ConnectStatus"),R=a("ExpireProgress"),U=a("el-switch"),x=a("Refresh"),$=a("Edit"),I=a("Delete"),E=a("el-popconfirm"),F=a("el-table"),B=a("DataFormDialog"),f=a("DataDetailDialog"),z=a("AddressListgDialog");return u(),g("div",null,[o(F,ee({stripe:"",border:""},e.$attrs,{onSortChange:t[0]||(t[0]=r=>e.$emit("sort-change",r)),onSelectionChange:t[1]||(t[1]=r=>e.$emit("selection-change",r))}),{default:n(()=>[i.RoleEnum.Admin!=l.role?(u(),v(m,{key:0,type:"selection","header-align":"center",align:"center",width:"40",selectable:s.handleSelectable},null,8,["selectable"])):C("",!0),o(m,{label:e.$t("\u57DF\u540D"),"header-align":"center",align:"center",width:"230","show-overflow-tooltip":"",prop:"domain"},{header:n(()=>[o(V,{effect:"dark",content:"\u9ED8\u8BA4\u7AEF\u53E3\uFF1A443",placement:"top-start","show-after":800},{default:n(()=>[c("div",Ge,[c("span",Ne,_(e.$t("\u57DF\u540D")),1),o(p,null,{default:n(()=>[o(d)]),_:1})])]),_:1})]),default:n(r=>[o(y,{underline:!1,onClick:w=>s.handleShowDetail(r.row)},{default:n(()=>[c("span",null,_(r.row.domain),1),r.row.port!="443"?(u(),g("span",qe,":"+_(r.row.port),1)):C("",!0)]),_:2},1032,["onClick"])]),_:1},8,["label"]),o(m,{label:e.$t("\u4E3B\u673A\u6570\u91CF"),"header-align":"center",align:"center",width:"80",prop:"address_count"},{default:n(r=>[r.row.is_dynamic_host?(u(),g("span",je,"*")):C("",!0),o(y,{underline:!1,onClick:w=>s.handleShowAddressListgDialog(r.row)},{default:n(()=>[D(_(r.row.address_count||"-"),1)]),_:2},1032,["onClick"])]),_:1},8,["label"]),o(m,{label:e.$t("\u72B6\u6001"),"header-align":"center",align:"center",width:"80",sortable:"custom",prop:"expire_status"},{default:n(r=>[o(b,{value:r.row.expire_status,onOnClick:w=>s.handleShowAddressListgDialog(r.row)},null,8,["value","onOnClick"])]),_:1},8,["label"]),o(m,{label:e.$t("\u8BC1\u4E66\u5929\u6570"),"header-align":"center",align:"center",width:"110",sortable:"custom",prop:"expire_days"},{header:n(()=>[o(V,{effect:"dark",content:"\u5982\u6709\u591A\u4E2A\u4E3B\u673AIP\u5730\u5740\uFF0C\u6B64\u5904\u4EC5\u663E\u793A\u5230\u671F\u65F6\u95F4\u6700\u77ED\u7684\u8BC1\u4E66",placement:"top-start","show-after":800},{default:n(()=>[c("div",He,[c("span",Ye,_(e.$t("\u8BC1\u4E66\u5929\u6570")),1),o(p,null,{default:n(()=>[o(d)]),_:1})])]),_:1})]),default:n(r=>[o(R,{startTime:r.row.start_time,endTime:r.row.expire_time},null,8,["startTime","endTime"])]),_:1},8,["label"]),o(m,{label:e.$t("\u5206\u7EC4"),"header-align":"center",align:"center",width:"100",sortable:"custom",prop:"group_name"},{default:n(r=>[c("span",null,_(r.row.group_name||"-"),1)]),_:1},8,["label"]),o(m,{label:e.$t("\u5907\u6CE8"),"header-align":"center",align:"left",prop:"check_time","min-width":"100","show-overflow-tooltip":""},{default:n(r=>[c("span",null,_(r.row.alias||"-"),1)]),_:1},8,["label"]),o(m,{label:e.$t("\u66F4\u65B0\u65F6\u95F4"),"header-align":"center",align:"center",width:"120",prop:"update_time",sortable:"custom","show-overflow-tooltip":""},{default:n(r=>[c("span",null,_(r.row.update_time_label||"-"),1)]),_:1},8,["label"]),i.RoleEnum.Admin!=l.role?(u(),g(O,{key:1},[o(m,{label:e.$t("\u81EA\u52A8\u66F4\u65B0"),width:"120","header-align":"center",align:"center",sortable:"custom",prop:"auto_update"},{default:n(r=>[o(U,{disabled:!r.row.has_edit_permission,modelValue:r.row.auto_update,"onUpdate:modelValue":w=>r.row.auto_update=w,onChange:w=>s.handleAutoUpdateStatusChange(r.row,w)},null,8,["disabled","modelValue","onUpdate:modelValue","onChange"])]),_:1},8,["label"]),o(m,{label:e.$t("\u5230\u671F\u63D0\u9192"),width:"90","header-align":"center",align:"center",sortable:"custom",prop:"is_monitor"},{default:n(r=>[o(U,{disabled:!r.row.has_edit_permission,modelValue:r.row.is_monitor,"onUpdate:modelValue":w=>r.row.is_monitor=w,onChange:w=>s.handleMonitorStatusChange(r.row,w)},null,8,["disabled","modelValue","onUpdate:modelValue","onChange"])]),_:1},8,["label"])],64)):C("",!0),o(m,{label:e.$t("\u64CD\u4F5C"),width:"100","header-align":"center",align:"center"},{default:n(r=>[o(y,{underline:!1,type:"primary",class:"mr-sm",onClick:w=>s.handleUpdateRowDomainInfo(r.row)},{default:n(()=>[o(p,null,{default:n(()=>[o(x)]),_:1})]),_:2},1032,["onClick"]),i.RoleEnum.Admin!=l.role?(u(),g(O,{key:0},[o(y,{underline:!1,type:"primary",class:"mr-sm",disabled:!r.row.has_edit_permission,onClick:w=>s.handleEditRow(r.row)},{default:n(()=>[o(p,null,{default:n(()=>[o($)]),_:1})]),_:2},1032,["disabled","onClick"]),o(E,{title:`${e.$t("\u786E\u5B9A\u5220\u9664")}\uFF1F`,onConfirm:w=>s.handleDeleteClick(r.row),disabled:!r.row.has_edit_permission},{reference:n(()=>[o(y,{underline:!1,type:"danger",disabled:!r.row.has_edit_permission},{default:n(()=>[o(p,null,{default:n(()=>[o(I)]),_:1})]),_:2},1032,["disabled"])]),_:2},1032,["title","onConfirm","disabled"])],64)):C("",!0)]),_:1},8,["label"])]),_:1},16),o(B,{visible:i.dialogVisible,"onUpdate:visible":t[2]||(t[2]=r=>i.dialogVisible=r),row:i.currentRow,onOnSuccess:t[3]||(t[3]=r=>s.handleRefreshRow(i.currentRow))},null,8,["visible","row"]),o(f,{row:i.currentRow,visible:i.dialogDetailVisible,"onUpdate:visible":t[4]||(t[4]=r=>i.dialogDetailVisible=r),onOnSuccess:t[5]||(t[5]=r=>s.handleRefreshRow(i.currentRow))},null,8,["row","visible"]),i.currentRow?(u(),v(z,{key:0,role:l.role,domainId:i.currentRow.id,domainRow:i.currentRow,visible:i.AddressListgDialogVisible,"onUpdate:visible":t[6]||(t[6]=r=>i.AddressListgDialogVisible=r),onOnClose:t[7]||(t[7]=r=>s.handleRefreshRow(i.currentRow))},null,8,["role","domainId","domainRow","visible"])):C("",!0)])}const We=S(Pe,[["render",Me]]),Ke={name:"updateDomainInfo",props:{},components:{},data(){return{updateTimer:null}},computed:{disableUpdateButton(){return this.updateTimer!=null},updateText(){return this.disableUpdateButton?this.$t("\u6B63\u5728\u66F4\u65B0"):this.$t("\u5168\u90E8\u66F4\u65B0")}},methods:{async updateAllDomainCertInfoOfUser(){this.updateTimer=!0,await this.$http.updateAllDomainCertInfoOfUser()}},beforeUnmount(){clearInterval(this.updateTimer),this.updateTimer=null},created(){}};function Qe(e,t,l,h,i,s){const m=a("Refresh"),d=a("el-icon"),p=a("el-link");return u(),v(p,{underline:!1,type:"primary",onClick:s.updateAllDomainCertInfoOfUser,disabled:s.disableUpdateButton},{default:n(()=>[o(d,null,{default:n(()=>[o(m)]),_:1}),D(_(s.updateText),1)]),_:1},8,["onClick","disabled"])}const Xe=S(Ke,[["render",Qe]]),Je={name:"updateDomainInfo",props:{},components:{},data(){return{updateTimer:null}},computed:{disableUpdateButton(){return this.updateTimer!=null},updateText(){return this.disableUpdateButton?this.$t("\u6B63\u5728\u68C0\u67E5"):this.$t("\u8BC1\u4E66\u68C0\u67E5")}},methods:{async handleNotifyByEventId(){let e=this.$loading({lock:!0,text:"\u68C0\u67E5\u4E2D",fullscreen:!0});try{const t=await this.$http.handleNotifyByEventId({event_id:re.SSL_CERT_EXPIRE});t.ok&&this.$msg.success(`\u68C0\u67E5\u6E20\u9053\uFF1A${t.data.success}`)}catch(t){console.log(t)}finally{this.$nextTick(()=>{e.close()})}}},beforeUnmount(){clearInterval(this.updateTimer),this.updateTimer=null},created(){}};function Ze(e,t,l,h,i,s){const m=a("Position"),d=a("el-icon"),p=a("el-link");return u(),v(p,{underline:!1,type:"primary",onClick:s.handleNotifyByEventId,disabled:s.disableUpdateButton},{default:n(()=>[o(d,null,{default:n(()=>[o(m)]),_:1}),D(_(s.updateText),1)]),_:1},8,["onClick","disabled"])}const et=S(Je,[["render",Ze]]),tt={name:"ConditionFilter",props:{},components:{ConditionFilterGroup:de},data(){return{loading:!0,options:[{title:"\u8BC1\u4E66\u72B6\u6001",maxCount:1,field:"expire_days",selected:[],options:[{label:"\u5DF2\u8FC7\u671F",value:[null,3]},{label:"3\u5929\u5185\u8FC7\u671F",value:[0,3]},{label:"7\u5929\u5185\u8FC7\u671F",value:[0,7]},{label:"30\u5929\u5185\u8FC7\u671F",value:[0,30]}]},{title:"\u57DF\u540D\u5206\u7EC4",field:"group_ids",hidden:!0,selected:[],options:[]}]}},computed:{...q(P,{groupOptions:"getGroupOptions"})},methods:{async resetData(){const e=await this.$http.getGroupList();e.ok&&this.options.forEach(t=>{t.field=="group_ids"&&(e.data.list&&e.data.list.length>0?(t.options=e.data.list.map(l=>{let h=l.name;return{...l,value:l.id,label:h}}),t.hidden=!1):t.hidden=!0)}),this.loading=!1},handleChange(e){this.$emit("on-change",this.options)}},created(){this.resetData()}},ot={class:""};function lt(e,t,l,h,i,s){const m=a("ConditionFilterGroup"),d=T("loading");return A((u(),g("div",ot,[o(m,{options:i.options,onOnChange:s.handleChange},null,8,["options","onOnChange"])])),[[d,i.loading]])}const it=S(tt,[["render",lt]]),nt={name:"",props:{selectedRows:{type:Array,default:[]}},components:{},data(){return{loading:!1,form:{auto_update:!0,is_monitor:!0},rules:{}}},computed:{},methods:{initData(){let e=this.selectedRows.filter(l=>l.auto_update).length,t=this.selectedRows.filter(l=>l.is_monitor).length;e>this.selectedRows.length/2?this.form.auto_update=!0:this.form.auto_update=!1,t>this.selectedRows.length/2?this.form.is_monitor=!0:this.form.is_monitor=!1},handleCancel(){this.$emit("on-cancel")},async handleValueChange(e,t){let l={domain_ids:this.selectedRows.map(i=>i.id),field:e,value:t};const h=await this.$http.updateDomainFieldByIds(l);h.code==0?(this.$msg.success("\u64CD\u4F5C\u6210\u529F"),this.$emit("on-success")):this.$msg.error(h.msg)}},created(){this.initData()}},at={class:"text-center"},st={class:"text-center"};function rt(e,t,l,h,i,s){const m=a("el-switch"),d=a("el-form-item"),p=a("el-form"),V=a("el-button"),y=T("loading");return A((u(),g("div",null,[c("div",at,"\u5DF2\u9009\u4E2D\uFF1A"+_(l.selectedRows.length)+" \u6761\u6570\u636E",1),o(p,{class:"mt-md",ref:"form",inline:!0,model:i.form,rules:i.rules,"label-width":"80px"},{default:n(()=>[o(d,{label:e.$t("\u81EA\u52A8\u66F4\u65B0"),prop:"auto_update"},{default:n(()=>[o(m,{modelValue:i.form.auto_update,"onUpdate:modelValue":t[0]||(t[0]=b=>i.form.auto_update=b),onChange:t[1]||(t[1]=b=>s.handleValueChange("auto_update",b))},null,8,["modelValue"])]),_:1},8,["label"]),o(d,{label:e.$t("\u5230\u671F\u63D0\u9192"),prop:"is_monitor"},{default:n(()=>[o(m,{modelValue:i.form.is_monitor,"onUpdate:modelValue":t[2]||(t[2]=b=>i.form.is_monitor=b),onChange:t[3]||(t[3]=b=>s.handleValueChange("is_monitor",b))},null,8,["modelValue"])]),_:1},8,["label"])]),_:1},8,["model","rules"]),c("div",st,[o(V,{onClick:s.handleCancel},{default:n(()=>[D(_(e.$t("\u53D6\u6D88")),1)]),_:1},8,["onClick"])])])),[[y,i.loading]])}const dt=S(nt,[["render",rt]]),mt={name:"domain-list",props:{role:{type:Number,default:L.User}},components:{DataFormDialog:H,DataTable:We,SelectGroup:N,UpdateDomainInfo:Xe,CheckDomainInfo:et,ConditionFilter:it,DataCount:ue,ExportFileDialog:me,BatchUpdateForm:dt},data(){return{RoleEnum:L,dataApi:G,list:[],total:0,page:1,size:20,keyword:"",group_id:"",pageSizeCachekey:"pageSize",loading:!0,dialogVisible:!1,export_to_file_url:J(G.exportDomainToFile),order_type:"ascending",order_prop:"expire_days",hasInitData:!1,ConditionFilterParams:[],selectedRows:[],params:{},exportFileDialogVisible:!1,batchUpdateDialogVisible:!1}},computed:{...q(P,{groupOptions:"getGroupOptions"}),showBatchActionButton(){return!!(this.selectedRows&&this.selectedRows.length>0)}},methods:{...te(P,{updateGroupOptions:"updateGroupOptions"}),resetData(){this.page=1,this.getData()},refreshData(){this.getData()},async getData(){this.loading=!0;let e={page:this.page,size:this.size,group_id:this.group_id,keyword:this.keyword.trim(),order_type:this.order_type,order_prop:this.order_prop,role:this.role};for(let l of this.ConditionFilterParams)l.selected&&l.selected.length>0&&(l.maxCount==1?e[l.field]=l.selected[0]:e[l.field]=l.selected);this.params=e;const t=await this.$http.getDomainList(e);t.code==0?(this.list=t.data.list,this.total=t.data.total):this.$msg.error(t.msg),this.loading=!1},getGroupName(e){let t=this.groupOptions.find(l=>l.value==e);if(t)return t.name},async handleHttpRequest(e){let t=this.$loading({fullscreen:!0}),l=new FormData;l.append("file",e.file),(await this.$http.importDomainFromFile(l)).code==0&&(this.$msg.success("\u4E0A\u4F20\u6210\u529F\uFF0C\u540E\u53F0\u5BFC\u5165\u4E2D"),this.resetData(),this.$refs.ConditionFilter&&this.$refs.ConditionFilter.resetData(),this.updateGroupOptions()),t.close()},handleAddRow(){this.dialogVisible=!0},handleAddSuccess(){this.resetData()},async handleExportConfirm(e){const t=await this.$http.exportDomainFile({...this.params,ext:e.ext});t.ok&&se.saveAs(t.data.url,t.data.name)},handleExportToFile(){this.exportFileDialogVisible=!0},handleSearch(){this.resetData()},handleSizeChange(e){localStorage.setItem(this.pageSizeCachekey,e),this.resetData()},loadPageSize(){let e=localStorage.getItem(this.pageSizeCachekey);e&&(this.size=parseInt(e))},handleExceed(e){this.$refs.upload.clearFiles();const t=e[0];t.uid=ce(),this.handleHttpRequest({file:t})},handleSortChange({column:e,prop:t,order:l}){console.log(e,t,l),this.order_prop="",this.order_type="",l&&(this.order_type=l,this.order_prop=t),this.resetData()},async initData(){this.loadPageSize(),await this.updateGroupOptions(),this.hasInitData=!0,this.getData()},handleSelectionChange(e){this.selectedRows=e},handleConditionFilterChange(e){console.log(e),this.ConditionFilterParams=e,this.resetData()},async handleBatchDeleteConfirm(){let e=this.$loading({fullscreen:!0}),t={ids:this.selectedRows.map(l=>l.id)};try{const l=await this.$http.deleteDomainByIds(t);l.code==0?(this.$msg.success("\u64CD\u4F5C\u6210\u529F"),this.resetData()):this.$msg.error(l.msg)}catch(l){console.log(l)}finally{this.$nextTick(()=>{e.close()})}},async handleRefreshRow(e){let t={id:e.id};const l=await this.$http.getDomainById(t);if(l.ok){let h=this.list.findIndex(i=>i.id==e.id);this.list.splice(h,1,l.data),console.log(this.list)}},handleAddCert(){const e=this.$router.resolve({path:"/cert/issue-certificate-list"});window.open(e.href,"_blank")},handleEditCert(e){this.$router.push({name:"CertEdit",query:{id:e.id}})},handleShowBatchUpdateDialog(){this.batchUpdateDialogVisible=!0},handleBatchUpdateFormCancel(){this.batchUpdateDialogVisible=!1},handleBatchUpdateFormSuccess(){this.batchUpdateDialogVisible=!1,this.refreshData()}},created(){this.keyword=this.$route.query.keyword||this.keyword,this.initData()}},ut={class:"app-container"},ct={class:"flex",style:{"justify-content":"space-between"}},pt={key:0},_t={key:1},ht={key:0},ft={class:"flex mt-sm",style:{"align-items":"center"}},gt={class:"flex",style:{"margin-left":"auto"}},bt=c("div",{style:{position:"absolute",top:"0",left:"0",right:"0",bottom:"0"}},null,-1);function wt(e,t,l,h,i,s){const m=a("Plus"),d=a("el-icon"),p=a("el-button"),V=a("Search"),y=a("el-input"),b=a("ConditionFilter"),R=a("DataCount"),U=a("Delete"),x=a("el-link"),$=a("el-popconfirm"),I=a("Edit"),E=a("UpdateDomainInfo"),F=a("CheckDomainInfo"),B=a("Upload"),f=a("el-upload"),z=a("Download"),r=a("DataTable"),w=a("el-pagination"),Y=a("DataFormDialog"),M=a("ExportFileDialog"),W=a("BatchUpdateForm"),K=a("el-dialog"),Q=T("loading");return u(),g("div",ut,[c("div",ct,[i.RoleEnum.Admin==l.role?(u(),g("span",pt)):(u(),g("div",_t,[o(p,{type:"primary",onClick:s.handleAddRow},{default:n(()=>[o(d,null,{default:n(()=>[o(m)]),_:1}),D(_(e.$t("\u6DFB\u52A0")),1)]),_:1},8,["onClick"])])),o(y,{class:"ml-sm",style:{width:"260px"},modelValue:i.keyword,"onUpdate:modelValue":t[0]||(t[0]=k=>i.keyword=k),placeholder:e.$t("\u641C\u7D22\u57DF\u540D"),clearable:"",onKeypress:oe(s.handleSearch,["enter"]),onClear:s.handleSearch},{append:n(()=>[o(p,{onClick:s.handleSearch},{default:n(()=>[o(d,null,{default:n(()=>[o(V)]),_:1})]),_:1},8,["onClick"])]),_:1},8,["modelValue","placeholder","onKeypress","onClear"])]),i.RoleEnum.Admin==l.role?(u(),g("span",ht)):(u(),g(O,{key:1},[i.hasInitData?(u(),v(b,{key:0,class:"mt-md",ref:"ConditionFilter",onOnChange:s.handleConditionFilterChange},null,8,["onOnChange"])):C("",!0)],64)),c("div",ft,[o(R,{value:i.total},null,8,["value"]),c("div",gt,[s.showBatchActionButton?(u(),g(O,{key:0},[o($,{title:"\u786E\u5B9A\u5220\u9664\u9009\u4E2D\uFF1F",onConfirm:s.handleBatchDeleteConfirm},{reference:n(()=>[o(x,{underline:!1,type:"danger",class:"mr-sm"},{default:n(()=>[o(d,null,{default:n(()=>[o(U)]),_:1}),D("\u6279\u91CF\u5220\u9664")]),_:1})]),_:1},8,["onConfirm"]),o(x,{underline:!1,type:"primary",class:"mr-sm",onClick:s.handleShowBatchUpdateDialog},{default:n(()=>[o(d,null,{default:n(()=>[o(I)]),_:1}),D("\u6279\u91CF\u64CD\u4F5C")]),_:1},8,["onClick"])],64)):C("",!0),o(E,{onOnSuccess:s.resetData},null,8,["onOnSuccess"]),i.RoleEnum.Admin!=l.role?(u(),g(O,{key:1},[o(F,{class:"ml-sm",onOnSuccess:s.resetData},null,8,["onOnSuccess"]),o(x,{underline:!1,type:"primary",class:"ml-sm",style:{position:"relative"}},{default:n(()=>[o(d,null,{default:n(()=>[o(B)]),_:1}),D(_(e.$t("\u5BFC\u5165"))+" ",1),o(f,{ref:"upload",action:"action",accept:".txt,.csv,.xlsx",limit:1,"on-exceed":s.handleExceed,"show-file-list":!1,"http-request":s.handleHttpRequest},{default:n(()=>[bt]),_:1},8,["on-exceed","http-request"])]),_:1}),o(x,{underline:!1,type:"primary",class:"ml-sm",onClick:s.handleExportToFile},{default:n(()=>[o(d,null,{default:n(()=>[o(z)]),_:1}),D(_(e.$t("\u5BFC\u51FA")),1)]),_:1},8,["onClick"])],64)):C("",!0)])]),A(o(r,{class:"mt-sm",role:l.role,data:i.list,onOnSuccess:s.resetData,onOnRefreshRow:s.handleRefreshRow,onSortChange:s.handleSortChange,onSelectionChange:s.handleSelectionChange},null,8,["role","data","onOnSuccess","onOnRefreshRow","onSortChange","onSelectionChange"]),[[Q,i.loading]]),o(w,{class:"mt-md justify-center",background:"",layout:"total, sizes, prev, pager, next",total:i.total,"page-size":i.size,"onUpdate:pageSize":t[1]||(t[1]=k=>i.size=k),"current-page":i.page,"onUpdate:currentPage":t[2]||(t[2]=k=>i.page=k),onCurrentChange:s.getData,onSizeChange:s.handleSizeChange},null,8,["total","page-size","current-page","onCurrentChange","onSizeChange"]),o(Y,{visible:i.dialogVisible,"onUpdate:visible":t[3]||(t[3]=k=>i.dialogVisible=k),onOnSuccess:s.handleAddSuccess},null,8,["visible","onOnSuccess"]),o(M,{visible:i.exportFileDialogVisible,"onUpdate:visible":t[4]||(t[4]=k=>i.exportFileDialogVisible=k),onOnConfirm:s.handleExportConfirm},null,8,["visible","onOnConfirm"]),o(K,{title:"\u6279\u91CF\u64CD\u4F5C",modelValue:i.batchUpdateDialogVisible,"onUpdate:modelValue":t[5]||(t[5]=k=>i.batchUpdateDialogVisible=k),width:"400px",center:"","append-to-body":""},{default:n(()=>[i.batchUpdateDialogVisible?(u(),v(W,{key:0,selectedRows:i.selectedRows,onOnCancel:s.handleBatchUpdateFormCancel,onOnSuccess:s.handleBatchUpdateFormSuccess},null,8,["selectedRows","onOnCancel","onOnSuccess"])):C("",!0)]),_:1},8,["modelValue"])])}const Et=S(mt,[["render",wt]]);export{Et as default};

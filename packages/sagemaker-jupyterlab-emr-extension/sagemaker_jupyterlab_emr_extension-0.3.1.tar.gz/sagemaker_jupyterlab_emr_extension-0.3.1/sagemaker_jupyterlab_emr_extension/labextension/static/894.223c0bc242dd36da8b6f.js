"use strict";(self.webpackChunk_amzn_sagemaker_jupyterlab_emr_extension=self.webpackChunk_amzn_sagemaker_jupyterlab_emr_extension||[]).push([[894],{1894:(e,t,n)=>{n.r(t),n.d(t,{default:()=>bn});var a=n(9217),r=n(6029),o=n.n(r),l=n(1586),s=n(1837);const i="SelectedCell",c="HoveredCellClassname",d="SelectAuthContainer",u="SelectEMRAccessRoleContainer";var m;!function(e){e.emrConnect="sagemaker-studio:emr-connect",e.emrServerlessConnect="sagemaker-studio:emr-serverless-connect"}(m||(m={}));const p={width:850,height:500};var g;!function(e){e.name="name",e.id="id",e.status="status",e.creationDateTime="creationDateTime",e.arn="clusterArn"}(g||(g={}));const h="AccessDeniedException",v={tabName:"EMR Clusters",widgetTitle:"Connect to cluster",connectCommand:{label:"Connect",caption:"Connect to a cluster"},connectMessage:{errorTitle:"Error connecting to EMR cluster",successTitle:"Successfully connected to EMR cluster",errorDefaultMessage:"Error connecting to EMR cluster",successDefaultMessage:"Connected to EMR Cluster"},selectRoleErrorMessage:{noEmrExecutionRole:"No available EMR execution role found for the cluster. Please provide one in user profile settings.",noEmrAssumableRole:"No available EMR assumable role found for the cluster. Please provide one in user profile settings."},widgetConnected:"The notebook is connected to",defaultTooltip:"Select a cluster to connect to",widgetHeader:"Select a cluster to connect to. A code block will be added to the active cell and run automatically to establish the connection.",connectedWidgetHeader:"cluster. You can submit new jobs to run on the cluster.",connectButton:"Connect",learnMore:"Learn more",noResultsMatchingFilters:"There are no clusters matching the filter.",radioButtonLabels:{basicAccess:"Http basic authentication",RBAC:"Role-based access control",noCredential:"No credential"},fetchEmrRolesError:"Failed to fetch EMR assumable and execution roles",listClusterError:"Fail to list clusters, refresh the modal or try again later",noCluster:"No clusters are available",permissionError:"The IAM role SageMakerStudioClassicExecutionRole does not have permissions needed to list EMR clusters. Update the role with appropriate permissions and try again. Refer to the",selectCluster:"Select a cluster",selectAssumableRoleTitle:"Select an assumable role for cluster",selectRuntimeExecRoleTitle:"Select EMR runtime execution role for cluster",setUpRuntimeExecRole:"Please make sure you have run the prerequisite steps.",selectAuthTitle:"Select credential type for ",clusterButtonLabel:"Cluster",expandCluster:{MasterNodes:"Master nodes",CoreNodes:"Core nodes",NotAvailable:"Not available",NoTags:"No tags",SparkHistoryServer:"Spark History Server",TezUI:"Tez UI",Overview:"Overview",Apps:"Apps",ApplicationUserInterface:"Application user Interface",Tags:"Tags"},presignedURL:{link:"Link",error:"Error: ",retry:"Retry",sparkUIError:"Spark UI Link is not available or time out. Please try ",sshTunnelLink:"SSH tunnel",or:" or ",viewTheGuide:"view the guide",clusterNotReady:"Cluster is not ready. Please try again later.",clusterNotConnected:"No active cluster connection. Please connect to a cluster and try again.",clusterNotCompatible:"EMR version 5.33+ or 6.3.0+ required for direct Spark UI links. Try a compatible cluster, use "}},E="Cancel",f="Select an execution role",C="Select a cross account assumable role",b={name:"Name",id:"ID",status:"Status",creationTime:"Creation Time",createdOn:"Created On",accountId:"Account ID"},x="EMR Serverless Applications",y="No serverless applications are available",w="AccessDeniedException: Please contact your administrator to get permissions to List Applications",I="AccessDeniedException: Please contact your administrator to get permissions to get selected application details",R={Overview:"Overview",NotAvailable:"Not available",NoTags:"No tags",Tags:"Tags",ReleaseLabel:"Release Label",Architecture:"Architecture",InteractiveLivyEndpoint:"Interactive Livy Endpoint",MaximumCapacity:"Maximum Capacity",Cpu:"Cpu",Memory:"Memory",Disk:"Disk"},S=({handleClick:e,tooltip:t})=>o().createElement("div",{className:"EmrClusterContainer"},o().createElement(l.ToolbarButtonComponent,{className:"EmrClusterButton",tooltip:t,label:v.clusterButtonLabel,onClick:e,enabled:!0}));var A;!function(e){e.tab="Tab",e.enter="Enter",e.escape="Escape",e.arrowDown="ArrowDown"}(A||(A={}));var k=n(8278),N=n(1316),T=n(8564);const M={ModalBase:s.css`
  &.jp-Dialog {
    z-index: 1; /* Override default z-index so Dropdown menu is above the Modal */
  }
  .jp-Dialog-body {
    padding: var(--jp-padding-xl);
    .no-cluster-msg {
      padding: var(--jp-cell-collapser-min-height);
      margin: auto;
    }
  }
`,Header:s.css`
  width: 100%;
  display: contents;
  font-size: 0.5rem;
  h1 {
    margin: 0;
  }
`,HeaderButtons:s.css`
  display: flex;
  float: right;
`,ModalFooter:s.css`
  display: flex;
  justify-content: flex-end;
  background-color: var(--jp-layout-color2);
  padding: 12px 24px 12px 24px;
  button {
    margin: 5px;
  }
`,Footer:s.css`
  .jp-Dialog-footer {
    background-color: var(--jp-layout-color2);
    margin: 0;
  }
`,DismissButton:s.css`
  padding: 0;
  border: none;
  cursor: pointer;
`,DialogClassname:s.css`
  .jp-Dialog-content {
    width: 900px;
    max-width: none;
    max-height: none;
    padding: 0;
  }
  .jp-Dialog-header {
    padding: 24px 24px 12px 24px;
    background-color: var(--jp-layout-color2);
  }
  /* Hide jp footer so we can add custom footer with button controls. */
  .jp-Dialog-footer {
    display: none;
  }
`},D=({heading:e,headingId:t="modalHeading",className:n,shouldDisplayCloseButton:a=!1,onClickCloseButton:r,actionButtons:l})=>{let i=null,c=null;return a&&(i=o().createElement(k.z,{className:(0,s.cx)(M.DismissButton,"dismiss-button"),role:"button","aria-label":"close",onClick:r,"data-testid":"close-button"},o().createElement(N.closeIcon.react,{tag:"span"}))),l&&(c=l.map((e=>{const{className:t,component:n,onClick:a,label:r}=e;return n?o().createElement("div",{key:`${(0,T.v4)()}`},n):o().createElement(k.z,{className:t,type:"button",role:"button",onClick:a,"aria-label":r,key:`${(0,T.v4)()}`},r)}))),o().createElement("header",{className:(0,s.cx)(M.Header,n)},o().createElement("h1",{id:t},e),o().createElement("div",{className:(0,s.cx)(M.HeaderButtons,"header-btns")},c,i))};var L=n(1105);const P=({onCloseModal:e,onConnect:t,disabled:n})=>o().createElement("footer",{"data-analytics-type":"eventContext","data-analytics":"JupyterLab",className:M.ModalFooter},o().createElement(k.z,{"data-analytics-type":"eventDetail","data-analytics":"EMR-Modal-Footer-CancelButton",className:"jp-Dialog-button jp-mod-reject jp-mod-styled listcluster-cancel-btn",type:"button",onClick:e},E),o().createElement(k.z,{"data-analytics-type":"eventDetail","data-analytics":"EMR-Modal-Footer-ConnectButton",className:"jp-Dialog-button jp-mod-accept jp-mod-styled listcluster-connect-btn",type:"button",onClick:t,disabled:n},v.connectButton));class U{constructor(e="",t="",n="",a="",r="",o="",l=""){this.partition=e,this.service=t,this.region=n,this.accountId=a,this.resourceInfo=r,this.resourceType=o,this.resourceName=l}static getResourceInfo(e){const t=e.match(U.SPLIT_RESOURCE_INFO_REG_EXP);let n="",a="";return t&&(1===t.length?a=t[1]:(n=t[1],a=t[2])),{resourceType:n,resourceName:a}}static fromArnString(e){const t=e.match(U.ARN_REG_EXP);if(!t)throw new Error(`Invalid ARN format: ${e}`);const[,n,a,r,o,l]=t,{resourceType:s="",resourceName:i=""}=l?U.getResourceInfo(l):{};return new U(n,a,r,o,l,s,i)}static isValid(e){return!!e.match(U.ARN_REG_EXP)}static getArn(e,t,n,a,r,o){return`arn:${e}:${t}:${n}:${a}:${r}/${o}`}}U.ARN_REG_EXP=/^arn:(.*?):(.*?):(.*?):(.*?):(.*)$/,U.SPLIT_RESOURCE_INFO_REG_EXP=/^(.*?)[/:](.*)$/,U.VERSION_DELIMITER="/";const j=({cellData:e})=>{var t,n,a;const r=null===(t=e.status)||void 0===t?void 0:t.state;return"RUNNING"===(null===(n=e.status)||void 0===n?void 0:n.state)||"WAITING"===(null===(a=e.status)||void 0===a?void 0:a.state)?o().createElement("div",null,o().createElement("svg",{width:"10",height:"10"},o().createElement("circle",{cx:"5",cy:"5",r:"5",fill:"green"})),o().createElement("label",{htmlFor:"myInput"},"Running/Waiting")):o().createElement("div",null,o().createElement("label",{htmlFor:"myInput"},r))};var _,$,O,B,F,z,G;!function(e){e.Bootstrapping="BOOTSTRAPPING",e.Running="RUNNING",e.Starting="STARTING",e.Terminated="TERMINATED",e.TerminatedWithErrors="TERMINATED_WITH_ERRORS",e.Terminating="TERMINATING",e.Undefined="UNDEFINED",e.Waiting="WAITING"}(_||(_={})),function(e){e.AllStepsCompleted="All_Steps_Completed",e.BootstrapFailure="Bootstrap_Failure",e.InstanceFailure="Instance_Failure",e.InstanceFleetTimeout="Instance_Fleet_Timeout",e.InternalError="Internal_Error",e.StepFailure="Step_Failure",e.UserRequest="User_Request",e.ValidationError="Validation_Error"}($||($={})),function(e){e[e.SHS=0]="SHS",e[e.TEZUI=1]="TEZUI",e[e.YTS=2]="YTS"}(O||(O={})),function(e){e.None="None",e.Basic_Access="Basic_Access",e.RBAC="RBAC"}(B||(B={})),function(e){e.Success="Success",e.Fail="Fail"}(F||(F={})),function(e){e[e.Content=0]="Content",e[e.External=1]="External",e[e.Notebook=2]="Notebook"}(z||(z={})),function(e){e.Started="STARTED",e.Starting="STARTING",e.Created="CREATED",e.Creating="CREATING",e.Stopped="STOPPED",e.Stopping="STOPPING",e.Terminated="TERMINATED"}(G||(G={}));const H=b;var J=n(2510),V=n(4321);s.css`
  height: 100%;
  position: relative;
`;const W=s.css`
  margin-right: 10px;
`,K=(s.css`
  ${W}
  svg {
    width: 6px;
  }
`,s.css`
  background-color: var(--jp-layout-color2);
  label: ${c};
  cursor: pointer;
`),q=s.css`
  background-color: var(--jp-layout-color3);
  -webkit-touch-callout: none; /* iOS Safari */
  -webkit-user-select: none; /* Safari */
  -khtml-user-select: none; /* Konqueror HTML */
  -moz-user-select: none; /* Old versions of Firefox */
  -ms-user-select: none; /* Internet Explorer/Edge */
  user-select: none; /* Non-prefixed version, currently supported by Chrome, Opera and Firefox */
  label: ${i};
`,X=s.css`
  background-color: var(--jp-layout-color2);
  display: flex;
  padding: var(--jp-cell-padding);
  width: 100%;
  align-items: baseline;
  justify-content: start;
  /* box shadow */
  -moz-box-shadow: inset 0 -15px 15px -15px var(--jp-layout-color3);
  -webkit-box-shadow: inset 0 -15px 15px -15px var(--jp-layout-color3);
  box-shadow: inset 0 -15px 15px -15px var(--jp-layout-color3);
  /* Disable visuals for scroll */
  overflow-x: scroll;
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
  &::-webkit-scrollbar {
    display: none;
  }
`,Y={borderTop:"var(--jp-border-width) solid var(--jp-border-color1)",borderBottom:"var(--jp-border-width) solid var(--jp-border-color1)",borderRight:"var(--jp-border-width) solid var(--jp-border-color1)",display:"flex",boxSizing:"border-box",marginRight:"0px",padding:"2.5px",fontWeight:"initial",textTransform:"capitalize",color:"var(--jp-ui-font-color2)"},Z={display:"flex",flexDirection:"column",height:"max-content"},Q=s.css`
  display: flex;
`,ee={height:"max-content",display:"flex",overflow:"auto",padding:"var(--jp-cell-padding)"},te=({isSelected:e})=>e?o().createElement(N.caretDownIcon.react,{tag:"span"}):o().createElement(N.caretRightIcon.react,{tag:"span"}),ne=({dataList:e,tableConfig:t,selectedId:n,expandedView:a,noResultsView:l,showIcon:i,isLoading:c,columnConfig:d,onRowSelect:u,...m})=>{const p=(0,r.useRef)(null),g=(0,r.useRef)(null),[h,v]=(0,r.useState)(-1),[E,f]=(0,r.useState)(0);(0,r.useEffect)((()=>{var e,t;f((null===(e=null==g?void 0:g.current)||void 0===e?void 0:e.clientHeight)||28),null===(t=p.current)||void 0===t||t.recomputeRowHeights()}),[n,c,t.width,t.height]);const C=({rowData:e,...t})=>e?(0,J.defaultTableCellDataGetter)({rowData:e,...t}):null;return o().createElement(J.Table,{...m,...t,headerStyle:Y,ref:p,headerHeight:28,overscanRowCount:10,rowCount:e.length,rowData:e,noRowsRenderer:()=>l,rowHeight:({index:t})=>e[t].id&&e[t].id===n?E:28,rowRenderer:e=>{const{style:t,key:r,rowData:l,index:i,className:c}=e,d=n===l.id,u=h===i,m=(0,s.cx)(Q,c,{[q]:d,[K]:!d&&u});return d?o().createElement("div",{key:r,ref:g,style:{...t,...Z},onMouseEnter:()=>v(i),onMouseLeave:()=>v(-1),className:m},(0,V.Cx)({...e,style:{width:t.width,...ee}}),o().createElement("div",{className:X},a)):o().createElement("div",{key:r,onMouseEnter:()=>v(i),onMouseLeave:()=>v(-1)},(0,V.Cx)({...e,className:m}))},onRowClick:({rowData:e})=>u(e),rowGetter:({index:t})=>e[t]},d.map((({dataKey:t,label:a,disableSort:r,cellRenderer:l})=>o().createElement(J.Column,{key:t,dataKey:t,label:a,flexGrow:1,width:150,disableSort:r,cellDataGetter:C,cellRenderer:t=>((t,a)=>{const{rowIndex:r,columnIndex:l}=t,s=e[r].id===n,c=0===l;let d=null;return a&&(d=a({row:e[r],rowIndex:r,columnIndex:l,onCellSizeChange:()=>null})),c&&i?o().createElement(o().Fragment,null,o().createElement(te,{isSelected:s})," ",d):d})(t,l)}))))},ae=s.css`
  height: 100%;
  position: relative;
`,re=s.css`
  margin-right: 10px;
`,oe=(s.css`
  ${re}
  svg {
    width: 6px;
  }
`,s.css`
  text-align: center;
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  margin-right: -50%;
  transform: translate(-50%, -50%);
`),le=(s.css`
  background-color: var(--jp-layout-color2);
  label: ${c};
  cursor: pointer;
`,s.css`
  background-color: var(--jp-layout-color3);
  -webkit-touch-callout: none; /* iOS Safari */
  -webkit-user-select: none; /* Safari */
  -khtml-user-select: none; /* Konqueror HTML */
  -moz-user-select: none; /* Old versions of Firefox */
  -ms-user-select: none; /* Internet Explorer/Edge */
  user-select: none; /* Non-prefixed version, currently supported by Chrome, Opera and Firefox */
  label: ${i};
`,s.css`
  background-color: var(--jp-layout-color2);
  display: flex;
  padding: var(--jp-cell-padding);
  width: 100%;
  align-items: baseline;
  justify-content: start;

  /* box shadow */
  -moz-box-shadow: inset 0 -15px 15px -15px var(--jp-layout-color3);
  -webkit-box-shadow: inset 0 -15px 15px -15px var(--jp-layout-color3);
  box-shadow: inset 0 -15px 15px -15px var(--jp-layout-color3);

  /* Disable visuals for scroll */
  overflow-x: scroll;
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
  &::-webkit-scrollbar {
    display: none;
  }
`,s.css`
  padding: 24px 24px 12px 24px;
`),se=s.css`
  .ReactVirtualized__Table__headerRow {
    display: flex;
  }
  .ReactVirtualized__Table__row {
    display: flex;
    font-size: 12px;
    align-items: center;
  }
`,ie=s.css`
  width: 100%;
  display: flex;
  flex-direction: row;
`,ce=s.css`
  flex-direction: column;
  margin: 0 32px 8px 8px;
  flex: 1 0 auto;
  width: 33%;
`,de=s.css`
  width: 20%;
`,ue=s.css`
  margin-bottom: var(--jp-code-padding);
`,me=v.expandCluster,pe=({clusterData:e})=>{const t=null==e?void 0:e.tags;return(null==t?void 0:t.length)?o().createElement(o().Fragment,null,t.map((e=>o().createElement("div",{className:ue,key:null==e?void 0:e.key},null==e?void 0:e.key,": ",null==e?void 0:e.value)))):o().createElement("div",null,me.NoTags)},ge=v.expandCluster;var he=n(2663),ve=n(7281);const Ee="/aws/sagemaker/api/emr/describe-cluster",fe="/aws/sagemaker/api/emr/get-on-cluster-app-ui-presigned-url",Ce="/aws/sagemaker/api/emr/create-persistent-app-ui",be="/aws/sagemaker/api/emr/describe-persistent-app-ui",xe="/aws/sagemaker/api/emr/get-persistent-app-ui-presigned-url",ye="/aws/sagemaker/api/emr/list-instance-groups",we="/aws/sagemaker/api/sagemaker/fetch-emr-roles",Ie="/aws/sagemaker/api/emr-serverless/get-application",Re=[200,201];var Se;!function(e){e.POST="POST",e.GET="GET",e.PUT="PUT"}(Se||(Se={}));const Ae=async(e,t,n)=>{const a=he.ServerConnection.makeSettings(),r=ve.URLExt.join(a.baseUrl,e);try{const e=await he.ServerConnection.makeRequest(r,{method:t,body:n},a);if(!Re.includes(e.status)&&r.includes("list-clusters"))throw 400===e.status?new Error("permission error"):new Error("Unable to fetch data");return e.json()}catch(e){return{error:e}}},ke=async e=>{var t;const n=JSON.stringify({}),a=await Ae(we,Se.POST,n);if((null===(t=null==a?void 0:a.EmrAssumableRoleArns)||void 0===t?void 0:t.length)>0)return a.EmrAssumableRoleArns.filter((t=>U.fromArnString(t).accountId===e))},Ne="ApplicationMaster",Te=async(e,t)=>{if(void 0===e)throw new Error("Error describing persistent app UI: Invalid persistent app UI ID");if(t){const n={PersistentAppUIId:e,RoleArn:t},a=JSON.stringify(n);return await Ae(be,Se.POST,a)}const n={PersistentAppUIId:e},a=JSON.stringify(n);return await Ae(be,Se.POST,a)},Me=async e=>await new Promise((t=>setTimeout(t,e))),De=async(e,t)=>{const n={ClusterId:e},a=await ke(t);if((null==a?void 0:a.length)>0)for(const t of a){const n=JSON.stringify({ClusterId:e,RoleArn:t}),a=await Ae(Ee,Se.POST,n);if(void 0!==(null==a?void 0:a.cluster))return a}const r=JSON.stringify(n);return await Ae(Ee,Se.POST,r)},Le="smsjp--icon-link-external",Pe={link:s.css`
  a& {
    color: var(--jp-content-link-color);
    line-height: var(--jp-custom-ui-text-line-height);
    text-decoration: none;
    text-underline-offset: 1.5px;

    span.${Le} {
      display: inline;
      svg {
        width: var(--jp-ui-font-size1);
        height: var(--jp-ui-font-size1);
        margin-left: var(--jp-ui-font-size1;
        transform: scale(calc(var(--jp-custom-ui-text-line-height) / 24));
      }
      path {
        fill: var(--jp-ui-font-color1);
      }
    }

    &.sm--content-link {
      text-decoration: underline;
    }

    &:hover:not([disabled]) {
      text-decoration: underline;
    }

    &:focus:not([disabled]),
    &:active:not([disabled]) {
      color: var(--jp-brand-color2);
      .${Le} path {
        fill: var(--jp-ui-font-color1);
      }
    }

    &:focus:not([disabled]) {
      border: var(--jp-border-width) solid var(--jp-brand-color2);
    }

    &:active:not([disabled]) {
      text-decoration: underline;
    }

    &[disabled] {
      color: var(--jp-ui-font-color3);
      .${Le} path {
        fill: var(--jp-ui-font-color1);
      }
    }
  }
`,externalIconClass:Le};var Ue;!function(e){e[e.Content=0]="Content",e[e.External=1]="External",e[e.Notebook=2]="Notebook"}(Ue||(Ue={}));const je=({children:e,className:t,disabled:n=!1,href:a,onClick:r,type:l=Ue.Content,hideExternalIcon:i=!1,...c})=>{const d=l===Ue.External,u={className:(0,s.cx)(Pe.link,t,{"sm-emr-content":l===Ue.Content}),href:a,onClick:n?void 0:r,target:d?"_blank":void 0,rel:d?"noopener noreferrer":void 0,...c},m=d&&!i?o().createElement("span",{className:Pe.externalIconClass},o().createElement(N.launcherIcon.react,{tag:"span"})):null;return o().createElement("a",{role:"link",...u},e,m)},_e=s.css`
  h2 {
    font-size: var(--jp-ui-font-size1);
    margin-top: 0;
  }
`,$e=s.css`
  .DataGrid-ContextMenu > div {
    overflow: hidden;
  }
  margin: 12px;
`,Oe=s.css`
  padding-bottom: var(--jp-add-tag-extra-width);
`,Be=s.css`
  background-color: var(--jp-layout-color2);
  display: flex;
  justify-content: flex-end;
  button {
    margin: 5px;
  }
`,Fe=s.css`
  text-align: center;
  vertical-align: middle;
`,ze=s.css`
  .jp-select-wrapper select {
    border: 1px solid;
  }
`,Ge={ModalBase:_e,ModalBody:$e,ModalFooter:Be,ListTable:s.css`
  overflow: hidden;
`,NoHorizontalPadding:s.css`
  padding-left: 0;
  padding-right: 0;
`,RadioGroup:s.css`
  display: flex;
  justify-content: flex-start;
  li {
    margin-right: 20px;
  }
`,ModalHeader:Oe,ModalMessage:Fe,AuthModal:s.css`
  min-height: none;
`,ListClusterModal:s.css`
  /* so the modal height remains the same visually during and after loading (this number can be changed) */
  min-height: 600px;
`,ConnectCluster:s.css`
  white-space: nowrap;
`,ClusterDescription:s.css`
  display: inline;
`,PresignedURL:s.css`
  line-height: normal;
`,ClusterListModalCrossAccountError:s.css`
  display: flex;
  flex-direction: column;
  padding: 0 0 10px 0;
`,GridWrapper:s.css`
  box-sizing: border-box;
  width: 100%;
  height: 100%;

  & .ReactVirtualized__Grid {
    /* important is required because react virtualized puts overflow style inline */
    overflow-x: hidden !important;
  }

  & .ReactVirtualized__Table__headerRow {
    display: flex;
  }

  & .ReactVirtualized__Table__row {
    display: flex;
    font-size: 12px;
    align-items: center;
  }
`,EmrExecutionRoleContainer:s.css`
  margin-top: 25px;
  width: 90%;
`,Dropdown:s.css`
  margin-top: var(--jp-cell-padding);
`,PresignedURLErrorText:s.css`
  color: var(--jp-error-color1);
`,DialogClassname:s.css`
  .jp-Dialog-content {
    width: 900px;
    max-width: none;
    max-height: none;
    padding: 0;
  }
  .jp-Dialog-header {
    padding: 24px 24px 12px 24px;
    background-color: var(--jp-layout-color2);
  }
  /* Hide jp footer so we can add custom footer with button controls. */
  .jp-Dialog-footer {
    display: none;
  }
`,Footer:s.css`
  .jp-Dialog-footer {
    background-color: var(--jp-layout-color2);
    margin: 0;
  }
`,SelectRole:ze},He="Invalid Cluster State",Je="Missing Cluster ID, are you connected to a cluster?",Ve="Unsupported cluster version",We=({clusterId:e,accountId:t,applicationId:n,persistentAppUIType:a,label:l,onError:i})=>{const[c,d]=(0,r.useState)(!1),[u,m]=(0,r.useState)(!1),p=(0,r.useCallback)((e=>{m(!0),i(e)}),[i]),g=(0,r.useCallback)((e=>{if(!e)throw new Error("Error opening Spark UI: Invalid URL");null!==window.open(e,"_blank","noopener,noreferrer")&&(m(!1),i(null))}),[i]),h=(0,r.useCallback)(((e,t,n)=>{(async(e,t,n)=>{const a=await ke(e);if((null==a?void 0:a.length)>0)for(const e of a){const a={ClusterId:t,OnClusterAppUIType:Ne,ApplicationId:n,RoleArn:e},r=JSON.stringify(a),o=await Ae(fe,Se.POST,r);if(void 0!==(null==o?void 0:o.presignedURL))return o}const r={ClusterId:t,OnClusterAppUIType:Ne,ApplicationId:n},o=JSON.stringify(r);return await Ae(fe,Se.POST,o)})(t,e,n).then((e=>g(null==e?void 0:e.presignedURL))).catch((e=>p(e))).finally((()=>d(!1)))}),[p,g]),E=(0,r.useCallback)(((e,t,n,a)=>{(async e=>{if(void 0===e)throw new Error("Error describing persistent app UI: Invalid persistent app UI ID");const t=U.fromArnString(e).accountId,n=await ke(t);if((null==n?void 0:n.length)>0)for(const t of n){const n={TargetResourceArn:e,RoleArn:t},a=JSON.stringify(n),r=await Ae(Ce,Se.POST,a);if(void 0!==(null==r?void 0:r.persistentAppUIId))return r}const a={TargetResourceArn:e},r=JSON.stringify(a);return await Ae(Ce,Se.POST,r)})(e.clusterArn).then((e=>(async(e,t,n,a)=>{var r;const o=Date.now();let l,s=0;for(;s<=3e4;){const t=await Te(e,a),n=null===(r=null==t?void 0:t.persistentAppUI)||void 0===r?void 0:r.persistentAppUIStatus;if(n&&"ATTACHED"===n){l=t;break}await Me(2e3),s=Date.now()-o}if(null==l)throw new Error("Error waiting for persistent app UI ready: Max attempts reached");return l})(null==e?void 0:e.persistentAppUIId,0,0,null==e?void 0:e.roleArn))).then((e=>(async(e,t,n,a)=>{if(void 0===e)throw new Error("Error getting persistent app UI presigned URL: Invalid persistent app UI ID");if(t){const a={PersistentAppUIId:e,PersistentAppUIType:n,RoleArn:t},r=JSON.stringify(a);return await Ae(xe,Se.POST,r)}const r={PersistentAppUIId:e,PersistentAppUIType:n},o=JSON.stringify(r);return await Ae(xe,Se.POST,o)})(null==e?void 0:e.persistentAppUI.persistentAppUIId,null==e?void 0:e.roleArn,a))).then((e=>g(null==e?void 0:e.presignedURL))).catch((e=>p(e))).finally((()=>d(!1)))}),[p,g]),f=(0,r.useCallback)(((e,t,n,a)=>async()=>{if(d(!0),!t)return d(!1),void p(Je);const r=await De(t,e).catch((e=>p(e)));if(!r||!(null==r?void 0:r.cluster))return void d(!1);const o=null==r?void 0:r.cluster;if(o.releaseLabel)try{const e=o.releaseLabel.substr(4).split("."),t=+e[0],n=+e[1];if(t<5)return d(!1),void p(Ve);if(5===t&&n<33)return d(!1),void p(Ve);if(6===t&&n<3)return d(!1),void p(Ve)}catch(e){}switch(o.status.state){case _.Running:case _.Waiting:n?h(t,e,n):E(o,e,n,a);break;case _.Terminated:E(o,e,n,a);break;default:d(!1),p(He)}}),[h,E,p]);return o().createElement(o().Fragment,null,c?o().createElement("span",null,o().createElement(L.CircularProgress,{size:"1rem"})):o().createElement(je,{"data-analytics-type":"eventDetail","data-analytics":"EMR-Modal-PresignedUrl-Click",className:(0,s.cx)("PresignedURL",Ge.PresignedURL),onClick:f(t,e,n,a)},u?o().createElement("span",null,l&&l," ",o().createElement("span",{className:(0,s.cx)("PresignedURLErrorText",Ge.PresignedURLErrorText),onClick:f(t,e,n,a)},"(",v.presignedURL.retry,")")):l||v.presignedURL.link))},Ke=s.css`
  cursor: pointer;
  & {
    color: var(--jp-content-link-color);
    text-decoration: none;
    text-underline-offset: 1.5px;
    text-decoration: underline;

    &:hover:not([disabled]) {
      text-decoration: underline;
    }

    &:focus:not([disabled]) {
      border: var(--jp-border-width) solid var(--jp-brand-color2);
    }

    &:active:not([disabled]) {
      text-decoration: underline;
    }

    &[disabled] {
      color: var(--jp-ui-font-color3);
    }
  }
`,qe=s.css`
  display: flex;
`,Xe=(s.css`
  margin-left: 10px;
`,s.css`
  margin-bottom: var(--jp-code-padding);
`),Ye=v.expandCluster,Ze=({clusterId:e,accountId:t,setIsError:n})=>{const[a]=(0,r.useState)(!1);return o().createElement("div",{className:qe},o().createElement("div",{className:(0,s.cx)("HistoryLink",Ke)},o().createElement(We,{clusterId:e,onError:e=>e,accountId:t,persistentAppUIType:"SHS",label:Ye.SparkHistoryServer})),o().createElement(N.launcherIcon.react,{tag:"span"}),a&&o().createElement("span",null,o().createElement(L.CircularProgress,{size:"1rem"})))},Qe=v.expandCluster,et=({clusterId:e,accountId:t,setIsError:n})=>{const[a]=o().useState(!1);return o().createElement("div",{className:qe},o().createElement("div",{className:Ke},o().createElement(We,{clusterId:e,onError:e=>e,accountId:t,persistentAppUIType:"TEZ",label:Qe.TezUI})),o().createElement(N.launcherIcon.react,{tag:"span"}),a&&o().createElement("span",null,o().createElement(L.CircularProgress,{size:"1rem"})))},tt=v.expandCluster,nt=e=>{const{accountId:t,selectedClusterId:n}=e,[a,l]=(0,r.useState)(!1);return a?o().createElement("div",null,tt.NotAvailable):o().createElement(o().Fragment,null,o().createElement("div",{className:Xe},o().createElement(Ze,{clusterId:n,accountId:t,setIsError:l})),o().createElement("div",{className:Xe},o().createElement(et,{clusterId:n,accountId:t,setIsError:l})))},at=v.expandCluster,rt=({clusterArn:e,accountId:t,selectedClusterId:n,clusterData:a})=>{const l=a,[i,c]=(0,r.useState)();return(0,r.useEffect)((()=>{(async e=>{var n,a;const r=JSON.stringify({ClusterId:e}),o=await Ae(ye,Se.POST,r);if((null===(n=o.instanceGroups)||void 0===n?void 0:n.length)>0&&(null===(a=o.instanceGroups[0].id)||void 0===a?void 0:a.length)>0)c(o);else{const n=await ke(t);if((null==n?void 0:n.length)>0)for(const t of n){const n=JSON.stringify({ClusterId:e,RoleArn:t}),a=await Ae(ye,Se.POST,n);a.instanceGroups.length>0&&a.instanceGroups[0].id&&c(a)}}})(n)}),[n]),o().createElement("div",{"data-analytics-type":"eventContext","data-analytics":"JupyterLab",className:ie},o().createElement("div",{className:ce},o().createElement("h4",null,at.Overview),o().createElement("div",{className:ue},(e=>{var t;const n=null===(t=null==e?void 0:e.instanceGroups)||void 0===t?void 0:t.find((e=>"MASTER"===(null==e?void 0:e.instanceGroupType)));if(n){const e=n.runningInstanceCount,t=n.instanceType;return`${ge.MasterNodes}: ${e}, ${t}`}return`${ge.MasterNodes}: ${ge.NotAvailable}`})(i)),o().createElement("div",{className:ue},(e=>{var t;const n=null===(t=null==e?void 0:e.instanceGroups)||void 0===t?void 0:t.find((e=>"CORE"===(null==e?void 0:e.instanceGroupType)));if(n){const e=n.runningInstanceCount,t=n.instanceType;return`${ge.CoreNodes}: ${e}, ${t}`}return`${ge.CoreNodes}: ${ge.NotAvailable}`})(i)),o().createElement("div",{className:ue},at.Apps,": ",(e=>{const t=null==e?void 0:e.applications;return(null==t?void 0:t.length)?t.map(((e,n)=>{const a=n===t.length-1?".":", ";return`${null==e?void 0:e.name} ${null==e?void 0:e.version}${a}`})):`${ge.NotAvailable}`})(l))),o().createElement("div",{className:(0,s.cx)(ce,de)},o().createElement("h4",null,at.ApplicationUserInterface),o().createElement(nt,{selectedClusterId:n,accountId:t,clusterArn:e})),o().createElement("div",{className:ce},o().createElement("h4",null,at.Tags),o().createElement(pe,{clusterData:a})))},ot=v,lt=o().createElement("div",{className:ae},o().createElement("p",{className:oe},ot.noResultsMatchingFilters)),st=({clustersList:e,tableConfig:t,clusterManagementListConfig:n,selectedClusterId:a,clusterArn:r,accountId:l,onRowSelect:s,clusterDetails:i,...c})=>{const d=!i&&!1,u=i;return o().createElement(ne,{...c,tableConfig:t,showIcon:!0,dataList:e,selectedId:a,columnConfig:n,isLoading:d,noResultsView:lt,onRowSelect:s,expandedView:d?o().createElement("span",null,o().createElement(L.CircularProgress,{size:"1rem"})):o().createElement(rt,{selectedClusterId:a,accountId:l||"",clusterArn:r,clusterData:u,instanceGroupData:void 0})})};n(7960);const it=e=>"string"==typeof e&&e.length>0,ct=e=>Array.isArray(e)&&e.length>0,dt=(e,t)=>{window&&window.panorama&&window.panorama("trackCustomEvent",{eventType:"eventDetail",eventDetail:e,eventContext:t,timestamp:Date.now()})},ut=(e,t,n)=>{t.execute(e,n)},mt=e=>t=>n=>{ut(e,t,n)},pt=Object.fromEntries(Object.entries(m).map((e=>{const t=e[0],n=e[1];return[t,(a=n,{id:a,createRegistryWrapper:mt(a),execute:(e,t)=>ut(a,e,t)})];var a}))),gt=({onCloseModal:e,selectedCluster:t,selectedServerlessApplication:n,emrConnectRoleData:a,app:l,selectedAssumableRoleArn:i})=>{const c=`${u}`,d=t?a.EmrExecutionRoleArns.filter((e=>U.fromArnString(e).accountId===t.clusterAccountId)):n?a.EmrExecutionRoleArns.filter((e=>U.fromArnString(e).accountId===U.fromArnString(n.arn).accountId)):[],m=d.length?d[0]:void 0,[p,g]=(0,r.useState)(m),h=d.length?o().createElement(N.HTMLSelect,{className:(0,s.cx)(Ge.SelectRole),options:d,value:p,title:f,onChange:e=>{g(e.target.value)},"data-testid":"select-runtime-exec-role"}):o().createElement("span",{className:"error-msg"},v.selectRoleErrorMessage.noEmrExecutionRole);return o().createElement("div",{className:(0,s.cx)(c,Ge.ModalBase,Ge.AuthModal)},o().createElement("div",{className:(0,s.cx)(c,Ge.ModalBody,Ge.SelectRole)},h),o().createElement("div",{className:(0,s.cx)(c,Ge.ModalBody)},o().createElement(je,{href:t?"https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-steps-runtime-roles.html#emr-steps-runtime-roles-configure":n?"https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/getting-started.html#gs-runtime-role":"",type:Ue.External},v.setUpRuntimeExecRole)),o().createElement(P,{onCloseModal:e,onConnect:()=>{if(e(),t){const e={clusterId:t.id,language:"python",authType:B.Basic_Access,executionRoleArn:p};i&&Object.assign(e,{crossAccountArn:i}),l.commands.execute(pt.emrConnect.id,e),dt("EMR-Connect-RBAC","JupyterLab")}else if(n){const e={serverlessApplicationId:n.id,executionRoleArn:p,language:"python",assumableRoleArn:i};l.commands.execute(pt.emrServerlessConnect.id,e)}},disabled:void 0===p}))},ht=({onCloseModal:e,selectedCluster:t,emrConnectRoleData:n,app:a,selectedAssumableRoleArn:l})=>{const i=`${d}`,c=`${d}`,[u,m]=(0,r.useState)(B.Basic_Access);return o().createElement("div",{className:(0,s.cx)(i,Ge.ModalBase,Ge.AuthModal)},o().createElement("div",{className:(0,s.cx)(c,Ge.ModalBody)},o().createElement(L.FormControl,null,o().createElement(L.RadioGroup,{"aria-labelledby":"demo-radio-buttons-group-label",defaultValue:B.Basic_Access,value:u,onChange:e=>{m(e.target.value)},name:"radio-buttons-group","data-testid":"radio-button-group",row:!0},o().createElement(L.FormControlLabel,{"data-analytics-type":"eventDetail","data-analytics":"EMR-Modal-SelectAuth-BasicAccess-Click",value:B.Basic_Access,control:o().createElement(L.Radio,null),label:v.radioButtonLabels.basicAccess}),o().createElement(L.FormControlLabel,{"data-analytics-type":"eventDetail","data-analytics":"EMR-Modal-SelectAuth-RBAC-Click",value:B.RBAC,control:o().createElement(L.Radio,null),label:v.radioButtonLabels.RBAC}),!Boolean(null===(p=t.kerberosAttributes)||void 0===p?void 0:p.kdcAdminPassword)&&!(e=>{var t;return Boolean(null===(t=e.configurations)||void 0===t?void 0:t.some((e=>{var t;return"ldap"===(null===(t=null==e?void 0:e.properties)||void 0===t?void 0:t.livyServerAuthType)})))})(t)&&o().createElement(L.FormControlLabel,{"data-analytics-type":"eventDetail","data-analytics":"EMR-Modal-SelectAuth-None-Click",value:B.None,control:o().createElement(L.Radio,null),label:v.radioButtonLabels.noCredential})))),o().createElement(P,{onCloseModal:e,onConnect:()=>{if(u===B.RBAC)e(),Ct(n,a,l,t);else{e();const n={clusterId:t.id,authType:u,language:"python"};l&&Object.assign(n,{crossAccountArn:l}),a.commands.execute(pt.emrConnect.id,n),dt("EMR-Connect-Non-RBAC","JupyterLab")}},disabled:!1}));var p},vt=({onCloseModal:e,selectedCluster:t,selectedServerlessApplication:n,emrConnectRoleData:a,app:l})=>{const i=`${u}`,c=t?a.EmrAssumableRoleArns.filter((e=>U.fromArnString(e).accountId===t.clusterAccountId)):n?a.EmrAssumableRoleArns.filter((e=>U.fromArnString(e).accountId===U.fromArnString(n.arn).accountId)):[],d=c.length?c[0]:void 0,[m,p]=(0,r.useState)(d),g=c.length?o().createElement(N.HTMLSelect,{title:C,options:c,value:m,onChange:e=>{p(e.target.value)},"data-testid":"select-assumable-role"}):o().createElement("span",{className:"error-msg"},v.selectRoleErrorMessage.noEmrAssumableRole);return o().createElement("div",{className:(0,s.cx)(i,Ge.ModalBase,Ge.AuthModal)},o().createElement("div",{className:(0,s.cx)(i,Ge.ModalBody,Ge.SelectRole)},g),o().createElement(P,{onCloseModal:e,onConnect:()=>{e(),t?(ft(t,a,l,m),dt("EMR-Select-Assumable-Role","JupyterLab")):n&&Ct(a,l,m,void 0,n)},disabled:void 0===m}))},Et=(e,t,n,a)=>{let r={};const i=()=>r&&r.resolve();r=new l.Dialog({title:o().createElement(D,{heading:`${v.selectAssumableRoleTitle}`,shouldDisplayCloseButton:!0,onClickCloseButton:i}),body:o().createElement(vt,{onCloseModal:i,selectedCluster:n,selectedServerlessApplication:a,emrConnectRoleData:e,app:t})}),r.addClass((0,s.cx)(M.ModalBase,M.Footer,M.DialogClassname)),r.launch()},ft=(e,t,n,a)=>{let r={};const i=()=>r&&r.resolve();r=new l.Dialog({title:o().createElement(D,{heading:`${v.selectAuthTitle}"${e.name}"`,shouldDisplayCloseButton:!0,onClickCloseButton:i}),body:o().createElement(ht,{onCloseModal:i,selectedCluster:e,emrConnectRoleData:t,app:n,selectedAssumableRoleArn:a})}),r.addClass((0,s.cx)(M.ModalBase,M.Footer,M.DialogClassname)),r.launch()},Ct=(e,t,n,a,r)=>{let i={};const c=()=>i&&i.resolve();i=new l.Dialog({title:o().createElement(D,{heading:`${v.selectRuntimeExecRoleTitle}`,shouldDisplayCloseButton:!0,onClickCloseButton:c}),body:o().createElement(gt,{onCloseModal:c,selectedCluster:a,selectedServerlessApplication:r,emrConnectRoleData:e,app:t,selectedAssumableRoleArn:n})}),i.addClass((0,s.cx)(M.ModalBase,M.Footer,M.DialogClassname)),i.launch()},bt=e=>{const{onCloseModal:t,header:n,app:a}=e,[l,i]=(0,r.useState)([]),[c,d]=(0,r.useState)(!1),[u,m]=(0,r.useState)(""),[h,E]=(0,r.useState)(void 0),[f,C]=(0,r.useState)(),[b,x]=(0,r.useState)(""),[y,w]=(0,r.useState)(!0),I=[{dataKey:g.name,label:H.name,disableSort:!0,cellRenderer:({row:e})=>{var t,n;return((null===(t=e.name)||void 0===t?void 0:t.length)||0)>20?(null===(n=null==e?void 0:e.name)||void 0===n?void 0:n.slice(0,19))+"...":null==e?void 0:e.name}},{dataKey:g.id,label:H.id,disableSort:!0,cellRenderer:({row:e})=>null==e?void 0:e.id},{dataKey:g.status,label:H.status,disableSort:!0,cellRenderer:({row:e})=>o().createElement(j,{cellData:e})},{dataKey:g.creationDateTime,label:H.creationTime,disableSort:!0,cellRenderer:({row:e})=>{var t;return null===(t=null==e?void 0:e.status)||void 0===t?void 0:t.timeline.creationDateTime.split("+")[0].split(".")[0]}},{dataKey:g.arn,label:H.accountId,disableSort:!0,cellRenderer:({row:e})=>{if(null==e?void 0:e.clusterArn)return U.fromArnString(e.clusterArn).accountId}}],R=async(e="",t)=>{try{do{const n=JSON.stringify({ClusterStates:["RUNNING","WAITING"],...e&&{Marker:e},RoleArn:t}),a=await Ae("/aws/sagemaker/api/emr/list-clusters",Se.POST,n);a&&a.clusters&&i((e=>[...new Map([...e,...a.clusters].map((e=>[e.id,e]))).values()])),e=null==a?void 0:a.Marker}while(it(e))}catch(e){m(e.message)}};(0,r.useEffect)((()=>{(async()=>{var e;try{d(!0);const t=JSON.stringify({}),n=await Ae(we,Se.POST,t);if((null===(e=null==n?void 0:n.EmrAssumableRoleArns)||void 0===e?void 0:e.length)>0)for(const e of n.EmrAssumableRoleArns)await R("",e);await R(),d(!1)}catch(e){d(!1),m(e.message)}})()}),[]),(0,r.useEffect)((()=>{f&&E((async e=>{const t=S.find((t=>t.id===e));let n="";const a=null==t?void 0:t.clusterArn;a&&U.isValid(a)&&(n=U.fromArnString(a).accountId);const r=await De(e,n);(null==r?void 0:r.cluster.id)&&E(r.cluster)})(f))}),[f]);const S=(0,r.useMemo)((()=>null==l?void 0:l.sort(((e,t)=>{const n=e.name,a=t.name;return null==n?void 0:n.localeCompare(a)}))),[l]),A=(0,r.useCallback)((e=>{const t=S.find((t=>t.id===e));let n="";const a=null==t?void 0:t.clusterArn;return a&&U.isValid(a)&&(n=U.fromArnString(a).accountId),n}),[S]),k=(0,r.useCallback)((e=>{const t=S.find((t=>t.id===e)),n=null==t?void 0:t.clusterArn;return n&&U.isValid(n)?n:""}),[S]),N=(0,r.useCallback)((e=>{const t=null==e?void 0:e.id;t&&t===f?(C(t),x(""),w(!0)):(C(t),x(A(t)),w(!1),dt("EMR-Modal-ClusterRow","JupyterLab"))}),[f,A]);return o().createElement(o().Fragment,null,o().createElement("div",{"data-testid":"list-cluster-view"},u&&o().createElement("span",{className:"no-cluster-msg"},(e=>{const t=o().createElement("a",{href:"https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-configure-discoverability-emr-cluster.html"},"documentation");return e.includes("permission error")?o().createElement("span",{className:"error-msg"},v.permissionError," ",t):o().createElement("span",{className:"error-msg"},e)})(u)),c?o().createElement("span",null,o().createElement(L.CircularProgress,{size:"1rem"})):ct(l)?o().createElement("div",{className:(0,s.cx)(le,"modal-body-container")},n,o().createElement(o().Fragment,null,o().createElement("div",{className:(0,s.cx)(se,"grid-wrapper")},o().createElement(st,{clustersList:S,selectedClusterId:null!=f?f:"",clusterArn:k(null!=f?f:""),accountId:A(null!=f?f:""),tableConfig:p,clusterManagementListConfig:I,onRowSelect:N,clusterDetails:h})))):o().createElement("div",{className:"no-cluster-msg"},v.noCluster),o().createElement(P,{onCloseModal:t,onConnect:async()=>{try{const e=await Ae(we,Se.POST,void 0);if("MISSING_AWS_ACCOUNT_ID"===e.CallerAccountId)throw new Error("Failed to get caller account Id");if(!h)throw new Error("Error in getting cluster details");if(!b)throw new Error("Error in getting cluster account Id");h.clusterAccountId=b,h.clusterAccountId===e.CallerAccountId?(t(),ft(h,e,a)):(t(),Et(e,a,h)),dt("EMR-Select-Cluster","JupyterLab")}catch(e){m(e.message)}},disabled:y})))},xt=b,yt=({status:e})=>e===G.Started||e===G.Stopped||e===G.Created?o().createElement("div",null,o().createElement("svg",{width:"10",height:"10"},o().createElement("circle",{cx:"5",cy:"5",r:"5",fill:"green"})),o().createElement("label",{htmlFor:"myInput"},e)):o().createElement("div",null,o().createElement("label",{htmlFor:"myInput"},e)),wt=s.css`
  flex-direction: column;
  margin: 0 0 8px 8px;
  flex: 1 0 auto;
  width: 33%;
`,It=R;var Rt=n(4439),St=n.n(Rt);const At=R,kt=({applicationData:e})=>{const t=null==e?void 0:e.tags;return St().isEmpty(t)?o().createElement("div",null,At.NoTags):o().createElement(o().Fragment,null,Object.entries(t).map((([e,t])=>o().createElement("div",{className:ue,key:e},e,": ",t))))},Nt=R,Tt=({applicationData:e})=>e&&o().createElement(o().Fragment,null,o().createElement("div",{className:wt},o().createElement("h4",null,Nt.Overview),o().createElement("div",{className:ue},(e=>{const t=null==e?void 0:e.architecture;return t?`${It.Architecture}: ${t}`:`${It.Architecture}: ${It.NotAvailable}`})(e)),o().createElement("div",{className:ue},(e=>{const t=null==e?void 0:e.releaseLabel;return t?`${It.ReleaseLabel}: ${t}`:`${It.ReleaseLabel}: ${It.NotAvailable}`})(e)),o().createElement("div",{className:ue},(e=>{const t=null==e?void 0:e.livyEndpointEnabled;return"True"===t?`${It.InteractiveLivyEndpoint}: Enabled`:"False"===t?`${It.InteractiveLivyEndpoint}: Disabled`:`${It.InteractiveLivyEndpoint}: ${It.NotAvailable}`})(e))),o().createElement("div",{className:wt},o().createElement("h4",null,Nt.MaximumCapacity),o().createElement("div",{className:ue},(e=>{const t=null==e?void 0:e.maximumCapacityCpu;return t?`${It.Cpu}: ${t}`:`${It.Cpu}: ${It.NotAvailable}`})(e)),o().createElement("div",{className:ue},(e=>{const t=null==e?void 0:e.maximumCapacityMemory;return t?`${It.Memory}: ${t}`:`${It.Memory}: ${It.NotAvailable}`})(e)),o().createElement("div",{className:ue},(e=>{const t=null==e?void 0:e.maximumCapacityDisk;return t?`${It.Disk}: ${t}`:`${It.Disk}: ${It.NotAvailable}`})(e))),o().createElement("div",{className:wt},o().createElement("h4",null,Nt.Tags),o().createElement(kt,{applicationData:e}))),Mt=v,Dt=o().createElement("div",{className:ae},o().createElement("p",{className:oe},Mt.noResultsMatchingFilters)),Lt=({applicationsList:e,tableConfig:t,applicationManagementListConfig:n,selectedApplicationId:a,applicationArn:r,accountId:l,onRowSelect:s,applicationDetails:i,applicationDetailsLoading:c,...d})=>o().createElement(ne,{...d,tableConfig:t,showIcon:!0,dataList:e,selectedId:a,columnConfig:n,isLoading:c,noResultsView:Dt,onRowSelect:s,expandedView:c?o().createElement("span",null,o().createElement(L.CircularProgress,{size:"1rem"})):o().createElement(Tt,{applicationData:i})}),Pt=s.css`
  &:not(:active) {
    color: var(--jp-ui-font-color2);
  }
`,Ut=s.css`
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 16px;
  color: var(--jp-error-color0);
  background-color: var(--jp-error-color3);
`,jt=s.css`
  font-size: 12px;
  font-style: normal;
  font-weight: 500;
  line-height: 150%;
  margin: unset;
  flex-grow: 1;
`,_t=e=>{const[t,n]=(0,r.useState)(!1),{error:a}=e;return(0,r.useEffect)((()=>{n(!1)}),[a]),a&&!t?o().createElement("div",{className:Ut},o().createElement("p",{className:jt},a),o().createElement(L.IconButton,{sx:{padding:"4px",color:"inherit"},onClick:()=>{n(!0)}},o().createElement(N.closeIcon.react,{elementPosition:"center",tag:"span"}))):null},$t=e=>{const{onCloseModal:t,header:n,app:a}=e,[l,i]=(0,r.useState)([]),[c,d]=(0,r.useState)(!1),[u,m]=(0,r.useState)(""),[v,E]=(0,r.useState)(void 0),[f,C]=(0,r.useState)(!1),[b,x]=(0,r.useState)(),[R,S]=(0,r.useState)(""),[A,k]=(0,r.useState)(!0),N=[{dataKey:g.name,label:xt.name,disableSort:!0,cellRenderer:({row:e})=>{var t,n;return((null===(t=e.name)||void 0===t?void 0:t.length)||0)>20?(null===(n=null==e?void 0:e.name)||void 0===n?void 0:n.slice(0,19))+"...":null==e?void 0:e.name}},{dataKey:g.id,label:xt.id,disableSort:!0,cellRenderer:({row:e})=>null==e?void 0:e.id},{dataKey:g.status,label:xt.status,disableSort:!0,cellRenderer:({row:e})=>o().createElement(yt,{status:e.status})},{dataKey:g.creationDateTime,label:xt.creationTime,disableSort:!0,cellRenderer:({row:e})=>{var t;return null===(t=null==e?void 0:e.createdAt)||void 0===t?void 0:t.split("+")[0].split(".")[0]}},{dataKey:g.arn,label:xt.accountId,disableSort:!0,cellRenderer:({row:e})=>{if(null==e?void 0:e.arn)return U.fromArnString(e.arn).accountId}}],T=async(e="",t)=>{do{const n=JSON.stringify({states:[G.Started,G.Created,G.Stopped],...e&&{nextToken:e},roleArn:t}),a=await Ae("/aws/sagemaker/api/emr-serverless/list-applications",Se.POST,n);a&&a.applications&&i((e=>[...new Map([...e,...a.applications].map((e=>[e.id,e]))).values()])),e=null==a?void 0:a.nextToken,a.code||a.errorMessage?(d(!1),a.code===h?m(w):m(`${a.code}: ${a.errorMessage}`)):m("")}while(it(e))};(0,r.useEffect)((()=>{(async(e="")=>{var t;try{d(!0);const e=JSON.stringify({}),n=await Ae(we,Se.POST,e);if(await T(),(null===(t=null==n?void 0:n.EmrAssumableRoleArns)||void 0===t?void 0:t.length)>0)for(const e of n.EmrAssumableRoleArns)await T("",e);d(!1)}catch(e){d(!1),m(e.message)}})()}),[]);const M=(0,r.useMemo)((()=>null==l?void 0:l.sort(((e,t)=>{const n=e.name,a=t.name;return null==n?void 0:n.localeCompare(a)}))),[l]);(0,r.useEffect)((()=>{b&&E((async e=>{C(!0),k(!0);const t=l.find((t=>t.id===e));let n="";const a=null==t?void 0:t.arn;a&&U.isValid(a)&&(n=U.fromArnString(a).accountId);const r=await(async(e,t)=>{const n={applicationId:e},a=await ke(t);if((null==a?void 0:a.length)>0)for(const t of a){const n=JSON.stringify({applicationId:e,RoleArn:t}),a=await Ae(Ie,Se.POST,n);if(void 0!==(null==a?void 0:a.application))return a}const r=JSON.stringify(n);return await Ae(Ie,Se.POST,r)})(e,n);E(r.application),r.code||r.errorMessage?(C(!1),r.code===h?m(I):m(`${r.code}: ${r.errorMessage}`)):m(""),C(!1),k(!1)})(b))}),[b]);const D=(0,r.useCallback)((e=>{const t=M.find((t=>t.id===e));let n="";const a=null==t?void 0:t.arn;return a&&U.isValid(a)&&(n=U.fromArnString(a).accountId),n}),[M]),j=(0,r.useCallback)((e=>{const t=M.find((t=>t.id===e)),n=null==t?void 0:t.arn;return n&&U.isValid(n)?n:""}),[M]),_=(0,r.useCallback)((e=>{const t=null==e?void 0:e.id;t&&t===b?(x(t),S(""),k(!0)):(x(t),S(D(t)),k(!1))}),[b,D]);return o().createElement(o().Fragment,null,o().createElement("div",{"data-testid":"list-serverless-applications-view"},u&&o().createElement(_t,{error:u}),c?o().createElement("span",null,o().createElement(L.CircularProgress,{size:"1rem"})):ct(l)?o().createElement("div",{className:(0,s.cx)(le,"modal-body-container")},n,o().createElement(o().Fragment,null,o().createElement("div",{className:(0,s.cx)(se,"grid-wrapper")},o().createElement(Lt,{applicationsList:M,selectedApplicationId:null!=b?b:"",applicationArn:j(null!=b?b:""),accountId:D(null!=b?b:""),tableConfig:p,applicationManagementListConfig:N,onRowSelect:_,applicationDetails:v,applicationDetailsLoading:f})))):o().createElement("div",{className:"no-cluster-msg"},y),o().createElement(P,{onCloseModal:t,onConnect:async()=>{try{const e=await Ae(we,Se.POST);if("MISSING_AWS_ACCOUNT_ID"===e.CallerAccountId)throw new Error("Failed to get caller account Id");if(!v)throw new Error("Error in getting serverless application details");if(!R)throw new Error("Error in getting serverless application account Id");R!==e.CallerAccountId?(t(),Et(e,a,void 0,v)):(t(),Ct(e,a,void 0,void 0,v))}catch(e){m(e.message)}},disabled:A})))};function Ot(e){const{children:t,value:n,index:a,...r}=e;return o().createElement("div",{role:"tabpanel",hidden:n!==a,...r},n===a&&o().createElement("div",null,t))}function Bt(e){const[t,n]=o().useState(0);return o().createElement("div",null,o().createElement("div",null,o().createElement(L.Tabs,{value:t,onChange:(e,t)=>{n(t)}},o().createElement(L.Tab,{className:(0,s.cx)(Pt),label:x}),o().createElement(L.Tab,{className:(0,s.cx)(Pt),label:v.tabName}))),o().createElement(Ot,{value:t,index:0},o().createElement($t,{onCloseModal:e.onCloseModal,header:e.header,app:e.app})),o().createElement(Ot,{value:t,index:1},o().createElement(bt,{onCloseModal:e.onCloseModal,header:e.header,app:e.app})))}class Ft{constructor(e,t,n){this.disposeDialog=e,this.header=t,this.app=n}render(){return o().createElement(r.Suspense,{fallback:null},o().createElement(Bt,{onCloseModal:this.disposeDialog,app:this.app,header:this.header}))}}const zt=(e,t,n)=>new Ft(e,t,n);var Gt;!function(e){e["us-east-1"]="us-east-1",e["us-east-2"]="us-east-2",e["us-west-1"]="us-west-1",e["us-west-2"]="us-west-2",e["us-gov-west-1"]="us-gov-west-1",e["us-gov-east-1"]="us-gov-east-1",e["us-iso-east-1"]="us-iso-east-1",e["us-isob-east-1"]="us-isob-east-1",e["ca-central-1"]="ca-central-1",e["eu-west-1"]="eu-west-1",e["eu-west-2"]="eu-west-2",e["eu-west-3"]="eu-west-3",e["eu-central-1"]="eu-central-1",e["eu-north-1"]="eu-north-1",e["eu-south-1"]="eu-south-1",e["ap-east-1"]="ap-east-1",e["ap-south-1"]="ap-south-1",e["ap-southeast-1"]="ap-southeast-1",e["ap-southeast-2"]="ap-southeast-2",e["ap-southeast-3"]="ap-southeast-3",e["ap-northeast-3"]="ap-northeast-3",e["ap-northeast-1"]="ap-northeast-1",e["ap-northeast-2"]="ap-northeast-2",e["sa-east-1"]="sa-east-1",e["af-south-1"]="af-south-1",e["cn-north-1"]="cn-north-1",e["cn-northwest-1"]="cn-northwest-1",e["me-south-1"]="me-south-1"}(Gt||(Gt={}));const Ht=e=>(e=>e===Gt["cn-north-1"]||e===Gt["cn-northwest-1"])(e)?"https://docs.amazonaws.cn":"https://docs.aws.amazon.com",Jt=({clusterName:e})=>{const t=Ht(Gt["us-west-2"]);return o().createElement("div",{className:(0,s.cx)(Ge.ModalHeader,"list-cluster-modal-header")},(()=>{let t;if(e){const n=o().createElement("span",{className:Ge.ConnectCluster},e),a=`${v.widgetConnected} `,r=` ${v.connectedWidgetHeader} `;t=o().createElement("div",{className:(0,s.cx)(Ge.ClusterDescription,"list-cluster-description")},a,n,r)}else t=`${v.widgetHeader} `;return t})(),o().createElement(je,{href:`${t}/sagemaker/latest/dg/studio-notebooks-emr-cluster.html`,type:Ue.External},v.learnMore))};class Vt extends l.ReactWidget{constructor(e,t){super(),this.updateConnectedCluster=e=>{this._connectedCluster=e,this.update()},this.getToolTip=()=>this._connectedCluster?`${v.widgetConnected} ${this._connectedCluster.name} cluster`:v.defaultTooltip,this.clickHandler=async()=>{let e={};const t=()=>e&&e.resolve();e=new l.Dialog({title:o().createElement(D,{heading:v.widgetTitle,shouldDisplayCloseButton:!0,onClickCloseButton:t,className:"list-cluster-modal-header"}),body:zt(t,this.listClusterHeader(),this._appContext).render()}),e.handleEvent=t=>{"keydown"===t.type&&(({keyboardEvent:e,onEscape:t,onShiftTab:n,onShiftEnter:a,onTab:r,onEnter:o})=>{const{key:l,shiftKey:s}=e;s?l===A.tab&&n?n():l===A.enter&&a&&a():l===A.tab&&r?r():l===A.enter&&o?o():l===A.escape&&t&&t()})({keyboardEvent:t,onEscape:()=>e.reject()})},e.addClass((0,s.cx)(M.ModalBase,M.Footer,M.DialogClassname)),e.launch()},this.listClusterHeader=()=>{var e;return o().createElement(Jt,{clusterName:null===(e=this._connectedCluster)||void 0===e?void 0:e.name})},this._selectedCluster=null,this._appContext=t,this._connectedCluster=null,this._kernelId=null}get kernelId(){return this._kernelId}get selectedCluster(){return this._selectedCluster}updateKernel(e){this._kernelId!==e&&(this._kernelId=e,this.kernelId&&this.update())}render(){return o().createElement(S,{handleClick:this.clickHandler,tooltip:this.getToolTip()})}}const Wt=e=>null!=e,Kt=async(e,t,n=!0)=>new Promise((async(r,o)=>{if(t){const l=t.content,s=l.model,i=t.context.sessionContext,{metadata:c}=s.sharedModel.toJSON(),d={cell_type:"code",metadata:c,source:e},u=l.activeCell,m=u?l.activeCellIndex:0;if(s.sharedModel.insertCell(m,d),l.activeCellIndex=m,n)try{await a.NotebookActions.run(l,i)}catch(e){o(e)}const p=[];for(const e of u.outputArea.node.children)p.push(e.innerHTML);r({html:p,cell:u})}o("No notebook panel")})),qt=e=>{const t=e.shell.widgets("main");let n=t.next().value;for(;n;){if(n.hasClass("jp-NotebookPanel")&&n.isVisible)return n;n=t.next().value}return null};var Xt=n(7704),Yt=n.n(Xt);const Zt=e=>{const t=v.presignedURL.sshTunnelLink;return e?o().createElement(je,{href:e,type:Ue.External,hideExternalIcon:!0},t):o().createElement("span",{className:(0,s.cx)("PresignedURLErrorText",Ge.PresignedURLErrorText)},t)},Qt=()=>o().createElement(je,{href:"https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ssh-tunnel.html",type:Ue.External},v.presignedURL.viewTheGuide),en=({sshTunnelLink:e,error:t})=>o().createElement(o().Fragment,null,(()=>{switch(t){case He:return o().createElement("span",{className:(0,s.cx)("PresignedURLErrorText",Ge.PresignedURLErrorText)},o().createElement("b",null,v.presignedURL.error),v.presignedURL.clusterNotReady);case Je:return o().createElement("span",{className:(0,s.cx)("PresignedURLErrorText",Ge.PresignedURLErrorText)},o().createElement("b",null,v.presignedURL.error),v.presignedURL.clusterNotConnected);case Ve:return(e=>o().createElement("span",{className:(0,s.cx)("PresignedURLErrorText",Ge.PresignedURLErrorText)},o().createElement("b",null,v.presignedURL.error),v.presignedURL.clusterNotCompatible,Zt(e),v.presignedURL.or,Qt()))(e);default:return(e=>o().createElement("span",null,o().createElement("span",{className:(0,s.cx)("PresignedURLErrorText",Ge.PresignedURLErrorText)},o().createElement("b",null,v.presignedURL.error),v.presignedURL.sparkUIError),Zt(e),o().createElement("span",{className:(0,s.cx)("PresignedURLErrorText",Ge.PresignedURLErrorText)},v.presignedURL.or),Qt()))(e)}})()),tn=(e,t)=>{var n;for(let a=0;a<e.childNodes.length;a++)if(null===(n=e.childNodes[a].textContent)||void 0===n?void 0:n.includes(t))return a;return-1},nn=e=>{try{let t=e.lastElementChild;for(;t;)e.removeChild(t),t=e.lastElementChild}catch(e){}},an="YARN Application ID",rn="Spark UI",on="--cluster-id",ln="--assumable-role-arn",sn="%info",cn="%configure",dn={childList:!0,subtree:!0};class un{constructor(e){this.trackedPanels=new Set,this.trackedCells=new Set,this.notebookTracker=e,this.triggers=[mn,sn,cn],this.kernelChanged=!1,this.lastConnectedClusterId=null,this.lastConnectedAccountId=void 0}run(){this.notebookTracker.currentChanged.connect(((e,t)=>{t&&(this.isTrackedPanel(t)||(t.context.sessionContext.kernelChanged.connect(((e,t)=>{this.kernelChanged=!0})),t.context.sessionContext.iopubMessage.connect(((e,n)=>{!this.isTrackedPanel(t)||this.kernelChanged?(n?(this.trackPanel(t),this.handleExistingSparkWidgetsOnPanelLoad(t)):this.stopTrackingPanel(t),this.kernelChanged=!1):this.isTrackedPanel(t)&&this.checkMessageForEmrConnectAndInject(n,t)}))))}))}isTrackedCell(e){return this.trackedCells.has(e)}trackCell(e){this.trackedCells.add(e)}stopTrackingCell(e){this.trackedCells.delete(e)}isTrackedPanel(e){return this.trackedPanels.has(e)}trackPanel(e){this.trackedPanels.add(e)}stopTrackingPanel(e){this.trackedPanels.delete(e)}handleExistingSparkWidgetsOnPanelLoad(e){e.revealed.then((()=>{const t=new RegExp(this.triggers.join("|"));((e,t)=>{var n;const a=null===(n=null==e?void 0:e.content)||void 0===n?void 0:n.widgets;return null==a?void 0:a.filter((e=>{const n=e.model.sharedModel;return t.test(n.source)}))})(e,t).forEach((e=>{if(this.containsSparkMagicTable(e.outputArea.node)){const t=e.model.sharedModel,n=this.getClusterId(t.source),a=this.getAccountId(t.source);this.injectPresignedURL(e,n,a)}else this.injectPresignedURLOnTableRender(e)}))}))}checkMessageForEmrConnectAndInject(e,t){if("execute_input"!==e.header.msg_type)return;const n=e.content.code;var a;this.codeContainsTrigger(n)&&(a=n,t.content.widgets.filter((e=>e.model.sharedModel.source.includes(a)))).forEach((e=>{this.injectPresignedURLOnTableRender(e)}))}codeContainsTrigger(e){const t=this.triggers.filter((t=>e.includes(t)));return ct(t)}getParameterFromEmrConnectCommand(e,t){const n=e.split(" "),a=n.indexOf(t);if(!(-1===a||a+1>n.length-1))return n[a+1]}getClusterId(e){return e&&e.includes(on)?this.getParameterFromEmrConnectCommand(e,on)||null:this.lastConnectedClusterId}getAccountId(e){if(!e)return this.lastConnectedAccountId;if(e.includes(sn))return this.lastConnectedAccountId;if(e.includes(ln)){const t=this.getParameterFromEmrConnectCommand(e,ln);return void 0!==t?U.fromArnString(t).accountId:void 0}}getSparkMagicTableBodyNodes(e){const t=Array.from(e.getElementsByTagName("tbody"));return ct(t)?t.filter((e=>this.containsSparkMagicTable(e))):[]}containsSparkMagicTable(e){var t;return(null===(t=e.textContent)||void 0===t?void 0:t.includes(an))&&e.textContent.includes(rn)}isSparkUIErrorRow(e){var t;return e instanceof HTMLTableRowElement&&(null===(t=e.textContent)||void 0===t?void 0:t.includes(v.presignedURL.error))||!1}injectSparkUIErrorIntoNextTableRow(e,t,n,a){var r;const l=this.isSparkUIErrorRow(t.nextSibling);if(null===a)return void(l&&(null===(r=t.nextSibling)||void 0===r||r.remove()));let s;if(l?(s=t.nextSibling,nn(s)):s=((e,t)=>{let n=1,a=!1;for(let r=1;r<e.childNodes.length;r++)if(e.childNodes[r].isSameNode(t)){n=r,a=!0;break}if(!a)return null;const r=n+1<e.childNodes.length?n+1:-1;return e.insertRow(r)})(e,t),!s)return;const i=s.insertCell(),c=t.childElementCount;i.setAttribute("colspan",c.toString()),i.style.textAlign="left",i.style.background="#212121";const d=o().createElement(en,{sshTunnelLink:n,error:a});Yt().render(d,i)}injectPresignedURL(e,t,n){var a;const r=e.outputArea.node,l=e.model.sharedModel,s=this.getSparkMagicTableBodyNodes(r);if(!ct(s))return!1;if(l.source.includes(cn)&&s.length<2)return!1;for(let e=0;e<s.length;e++){const r=s[e],l=r.firstChild,i=tn(l,rn),c=tn(l,"Driver log"),d=tn(l,an),u=l.getElementsByTagName("th")[c];if(l.removeChild(u),-1===i||-1===d)break;for(let e=1;e<r.childNodes.length;e++){const l=r.childNodes[e],s=l.childNodes[i];l.childNodes[c].remove();const u=null===(a=s.getElementsByTagName("a")[0])||void 0===a?void 0:a.href;s.hasChildNodes()&&nn(s);const m=l.childNodes[d].textContent||void 0,p=document.createElement("div");s.appendChild(p);const g=o().createElement(We,{clusterId:t,applicationId:m,onError:e=>this.injectSparkUIErrorIntoNextTableRow(r,l,u,e),accountId:n});Yt().render(g,p)}}return!0}injectPresignedURLOnTableRender(e){this.isTrackedCell(e)||(this.trackCell(e),new MutationObserver(((t,n)=>{for(const a of t)if("childList"===a.type)try{const t=e.model.sharedModel,a=this.getClusterId(t.source),r=this.getAccountId(t.source);if(this.injectPresignedURL(e,a,r)){this.stopTrackingCell(e),n.disconnect(),this.lastConnectedClusterId=a,this.lastConnectedAccountId=r;break}}catch(t){this.stopTrackingCell(e),n.disconnect()}})).observe(e.outputArea.node,dn))}}const mn="%sm_analytics emr connect",pn=v,gn={id:"@sagemaker-studio:EmrCluster",autoStart:!0,optional:[a.INotebookTracker],activate:async(e,t)=>{null==t||new un(t).run(),e.docRegistry.addWidgetExtension("Notebook",new hn(e)),e.commands.addCommand(pt.emrConnect.id,{label:e=>pn.connectCommand.label,isEnabled:()=>!0,isVisible:()=>!0,caption:()=>pn.connectCommand.caption,execute:async t=>{try{const{clusterId:n,authType:a,language:r,crossAccountArn:o,executionRoleArn:l,notebookPanelToInjectCommandInto:s}=t,i="%load_ext sagemaker_studio_analytics_extension.magics",c=Wt(r)?`--language ${r}`:"",d=Wt(o)?`--assumable-role-arn ${o}`:"",u=Wt(l)?`--emr-execution-role-arn ${l}`:"",m=`${i}\n${mn} --verify-certificate False --cluster-id ${n} --auth-type ${a} ${c} ${d} ${u}`,p=s||qt(e);await Kt(m,p)}catch(e){throw e.message,e}}}),e.commands.addCommand(pt.emrServerlessConnect.id,{label:e=>pn.connectCommand.label,isEnabled:()=>!0,isVisible:()=>!0,caption:()=>pn.connectCommand.caption,execute:async t=>{try{const{serverlessApplicationId:n,language:a,assumableRoleArn:r,executionRoleArn:o,notebookPanelToInjectCommandInto:l}=t,s="%load_ext sagemaker_studio_analytics_extension.magics",i=Wt(a)?` --language ${a}`:"",c=`${s}\n%sm_analytics emr-serverless connect --application-id ${n}${i}${Wt(r)?` --assumable-role-arn ${r}`:""}${Wt(o)?` --emr-execution-role-arn ${o}`:""}`,d=l||qt(e);await Kt(c,d)}catch(e){throw e.message,e}}})}};class hn{constructor(e){this.appContext=e}createNew(e,t){const n=(a=e.sessionContext,r=this.appContext,new Vt(a,r));var a,r;return e.context.sessionContext.kernelChanged.connect((e=>{var t;const a=null===(t=e.session)||void 0===t?void 0:t.kernel;e.iopubMessage.connect(((e,t)=>{((e,t,n,a)=>{if(n)try{if(e.content.text){const{isConnSuccess:t,clusterId:r}=(e=>{let t,n=!1;if(e.content.text){const a=JSON.parse(e.content.text);if("sagemaker-analytics"!==a.namespace)return{};t=a.cluster_id,n=a.success}return{isConnSuccess:n,clusterId:t}})(e);t&&n.id===r&&a(n)}}catch(e){return}})(t,0,n.selectedCluster,n.updateConnectedCluster)})),a&&a.spec.then((e=>{e&&e.metadata&&n.updateKernel(a.id)})),n.updateKernel(null)})),e.toolbar.insertBefore("kernelName","emrCluster",n),n}}var vn=n(1085);const En={errorTitle:"Unable to connect to EMR cluster",defaultErrorMessage:"Something went wrong when connecting to the EMR cluster.",invalidRequestErrorMessage:"A request to attach the EMR cluster to the notebook is invalid.",invalidClusterErrorMessage:"EMR cluster ID is invalid."};let fn=!1;const Cn=async e=>(0,l.showErrorMessage)(En.errorTitle,{message:e}),bn=[gn,{id:"@sagemaker-studio:DeepLinking",requires:[vn.IRouter],autoStart:!0,activate:async(e,t)=>{const{commands:n}=e,a="emrCluster:open-notebook-for-deeplinking";n.addCommand(a,{execute:()=>(async(e,t)=>{if(!fn)try{const{search:n}=e.current;if(!n)return void await Cn(En.invalidRequestErrorMessage);t.restored.then((async()=>{const{clusterId:e,accountId:a}=ve.URLExt.queryStringToObject(n);if(!e)return void await Cn(En.invalidRequestErrorMessage);const r=await Ae(we,Se.POST,void 0);if(!r||(null==r?void 0:r.error))return void await Cn(v.fetchEmrRolesError);const o=await De(e);if(!o||!(null==o?void 0:o.cluster))return void await Cn(En.invalidClusterErrorMessage);const l=o.cluster,s=await t.commands.execute("notebook:create-new");await new Promise((e=>{s.sessionContext.kernelChanged.connect(((t,n)=>{e(n)}))})),await new Promise((e=>setTimeout(e,2e3))),a?(l.clusterAccountId=a,Et(r,t,l)):(l.clusterAccountId=r.CallerAccountId,ft(l,r,t))}))}catch(e){return void await Cn(En.defaultErrorMessage)}finally{fn=!0}})(t,e)}),t.register({command:a,pattern:new RegExp("[?]command=attach-emr-to-notebook"),rank:10})}}]}}]);
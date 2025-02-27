Adform.ADFBannerUtils = function(){
    this.initialize();
    this.tagID    = 0;
    this.banners  = new Object();
};

typeof Adform.ADFUtilInstance == "undefined" ? Adform.ADFUtilInstance=null:Adform.ADFUtilInstance=Adform.ADFUtilInstance;

Adform.ADFBannerUtils.getInstance = function() {
    if (Adform.ADFUtilInstance == null) {
        Adform.ADFUtilInstance = new Adform.ADFBannerUtils();
    }
    return Adform.ADFUtilInstance;
};

Adform.ADFBannerUtils.prototype.ADFCreateObjectCallback = function (obj, fn) { 
    return function() { fn.apply(obj, arguments); };
};

Adform.ADFBannerUtils.prototype.eventRegister = function(name, fname, object, obj) {
    if(object.addEventListener) object.addEventListener(name,this.ADFCreateObjectCallback(eval(obj), eval(fname)), false);
    else if (object.attachEvent) object.attachEvent("on"+name,this.ADFCreateObjectCallback(eval(obj), eval(fname)), false); 
};

Adform.ADFBannerUtils.prototype.addNewBanner = function(id, type){
    try{
        var banner = new Object({id:id, type:type});
        this.banners[id] = banner;
    } catch(e){try{/*new Image().src = Adform.host + "/adferror/?errmsg=Error in function ADFBannerUtils.addNewBanner " + e.message;*/}catch(e){}};   
};

Adform.ADFBannerUtils.prototype.addBannerAttribute = function(id, name, value){
    try{
        this.banners[id][name]=value;
    } catch(e){try{/*new Image().src = Adform.host + "/adferror/?errmsg=Error in function ADFBannerUtils.addBannerAttribute " + e.message;*/}catch(e){}};   
};

Adform.ADFBannerUtils.prototype.initialize = function() {
    try{
        //sets formation
        if(document.body == null){
            document.write("<html><body></body></html>");
        };
        this.ADFBrLa  = typeof navigator.browserLanguage !="undefined"?navigator.browserLanguage:typeof navigator.language !="undefined"?navigator.language:0;
        this.ADFOsLa  = typeof navigator.systemLanguage !="undefined"?navigator.systemLanguage:this.ADFBrLa;
        try{
            this.ADFSS    = screen?screen.width+"X"+screen.height:0;
            this.ADFSC    = screen?screen.colorDepth:0;
        }catch(e){
             this.ADFSS   = 0;
             this.ADFSC   = 0;
        };
        this.set1     = escape(this.ADFOsLa)+"|"+escape(this.ADFBrLa)+"|"+this.ADFSS+"|"+this.getFlashVersion();
        this.set2     = 50*Math.round(this.getWin().w/50)+"|"+50*Math.round(this.getWin().h/50)+"|"+this.ADFSC+"|"+this.getJSVersion()+"|"+this.getFlashVersion()+"|0|"+this.getCT()+"|"+this.getCPU()+"|0|0";
    } catch(e){try{/*new Image().src = Adform.host + "/adferror/?errmsg=Error in function ADFBannerUtils.initialize " + e.message;*/}catch(e){}};  
};

Adform.ADFBannerUtils.prototype.getTagID = function() {
    try{
        this.tagID++;
        return this.tagID+'x';
    } catch(e){try{/*new Image().src = Adform.host + "/adferror/?errmsg=Error in function getTagID " + e.message;*/}catch(e){}}; 
};

Adform.ADFBannerUtils.prototype.getJSVersion = function() {
    try {
        document.write('<span id="ADFtemp"></span>');
        for(var i= 1; i<10; i++){
            var adserveScript = document.createElement("script");
            adserveScript.setAttribute("language","javascript1." + i);
            adserveScript.text = "ADFJSVersion=" + (i+1) + ";";
            try{document.getElementById("ADFtemp").appendChild(adserveScript);}catch(e){};
        };
        try{document.getElementById('ADFtemp').parentNode.removeChild(document.getElementById("ADFtemp"))}catch(e){}; 
        return typeof ADFJSVersion != "undefined"?ADFJSVersion:1;
    } catch(e){try{/*new Image().src = Adform.host + "/adferror/?errmsg=Error in function ADFBannerUtils.getJSVersion " + e.message;*/}catch(e){}}; 
};

Adform.ADFBannerUtils.prototype.getFlashVersion = function(){
    try{
        var flashVersion = 0;
        // Having ActiveXObject, try to detect with it
        if( window.ActiveXObject ) {
        
            for( var i = 6; i < 12; i++ ) {
                    
                try{
                    new window.ActiveXObject( 'ShockwaveFlash.ShockwaveFlash.' + i );
                    flashVersion = i;
                } catch( error ) {
                    // Error
                }
            
            }
        // If having plugin
        } else if( navigator.plugins && navigator.plugins['Shockwave Flash'] && navigator.plugins['Shockwave Flash'].description ) {
        
            var matches = navigator.plugins['Shockwave Flash'].description.match( /([0-9]+)\.[0-9]+/ );
            
            if( matches[1] && ! isNaN( parseInt( matches[1] ) ) ) {
                flashVersion = parseInt( matches[1] );
            }
        
        };
        return flashVersion;
    } catch(e){try{/*new Image().src = Adform.host + "/adferror/?errmsg=Error in function ADFBannerUtils.getFlashVersion " + e.message;*/}catch(e){}}; 
};

Adform.ADFBannerUtils.prototype.getWin = function() {
    try{
        var retV = new Object();
        var d=window.document;
        if( typeof( window.innerWidth ) == 'number' ){
            retV.h = window.innerHeight;
            retV.w = window.innerWidth;
        } else if( d.documentElement && d.documentElement.clientHeight){
            retV.h  = d.documentElement.clientHeight;
            retV.w = d.documentElement.clientWidth;
        } else if( d.body && d.body.clientHeight){
            retV.h  = d.body.clientHeight;
            retV.w = d.body.clientWidth;
        };
        return retV;
    } catch(e){try{/*new Image().src = Adform.host + "/adferror/?errmsg=Error in function ADFBannerUtils.getWin " + e.message;*/}catch(e){}}; 
};
    
Adform.ADFBannerUtils.prototype.getCT = function () {
    try{
        var retV = new Object();
        retV["lan"]     ="1";
        retV["modem"]   ="2";
        var ADFCT="3";
        try{
            if(document.body.addBehavior){
                    document.body.addBehavior("#default#clientCaps");
                    ADFCT=document.body.connectionType.toLowerCase();
                    ADFCT=typeof retV[ADFCT] != "undefined"?retV[ADFCT]:ADFCT;
            
            }
        } catch(e){};
        return ADFCT;
    } catch(e){try{/*new Image().src = Adform.host + "/adferror/?errmsg=Error in function ADFBannerUtils.getCT " + e.message;*/}catch(e){}};
};

Adform.ADFBannerUtils.prototype.getCPU = function (){
    try{
        var retV = new Object();
        retV["x86"]     ="1";
        retV["68k"]     ="2";
        retV["PPC"]     ="3";
        retV["Alpha"]   ="4";
        retV["Arm"]     ="5";
        retV["Other"]   ="6";
        retV["7"]       ="7";
        var ADFCPU=(typeof(navigator.cpuClass)!="undefined")?navigator.cpuClass.toLowerCase():"7";
        return retV[ADFCPU] != "undefined"?retV[ADFCPU]:"8";
    } catch(e){try{/*new Image().src = Adform.host + "/adferror/?errmsg=Error in function ADFBannerUtils.getCPU " + e.message;*/}catch(e){}};
};

Adform.ADFBannerUtils.prototype.getSet1 = function () { 
    return this.set1;
};

Adform.ADFBannerUtils.prototype.getSet2 = function () { 
    return this.set2;
};

Adform.ADFBannerUtils.prototype.getPosition = function(temPlace){
    try{
        var retV = new Object();
        retV.y =temPlace.offsetTop;
        retV.x =temPlace.offsetLeft;
        var objParent;
        while(temPlace.offsetParent!=null){
            objParent=temPlace.offsetParent;	
            retV.y += (objParent.offsetTop);
            retV.x +=objParent.offsetLeft;
            temPlace=objParent;
        };
        return retV;
    } catch(e){try{/*new Image().src = Adform.host + "/adferror/?errmsg=Error in function ADFBannerUtils.getPosition " + e.message;*/}catch(e){}};
};

Adform.ADFBannerUtils.prototype.getScrollXY = function() {
    try{
        var retV = new Object({x:0, y:0});
        if( typeof( window.pageYOffset ) == 'number' ) {
            retV.y = window.pageYOffset;
            retV.x = window.pageXOffset;
        } else if( document.body && ( document.body.scrollLeft || document.body.scrollTop ) ) {
            retV.y = document.body.scrollTop;
            retV.x = document.body.scrollLeft;
        } else if( document.documentElement && ( document.documentElement.scrollLeft || document.documentElement.scrollTop ) ) {
            retV.y = document.documentElement.scrollTop;
            retV.x = document.documentElement.scrollLeft;
        };
        return retV;
    } catch(e){try{/*new Image().src = Adform.host + "/adferror/?errmsg=Error in function ADFBannerUtils.getScrollXY " + e.message;*/}catch(e){}};
};

Adform.ADFBannerUtils.prototype.getBrowser = function(){
    try{
        if(navigator.appVersion.indexOf("MSIE")!=-1&&navigator.userAgent.indexOf("Opera")<0){
            return "MSIE";
        };
        if(navigator.userAgent.indexOf("Safari")!=-1){
            return "Safari";
        };
        if(navigator.userAgent.indexOf("Opera")!=-1){
            return "Opera";
        };
        if(navigator.appName.indexOf("Netscape")!=-1){
            if((navigator.product.indexOf("Gecko")!=-1)&&((navigator.vendor.indexOf("Firefox")!=-1)||navigator.userAgent.indexOf("Firefox")!=-1)){
                return "Firefox";
            }else{
                return "Netscape";
            };
        };
    } catch(e){try{/*new Image().src = Adform.host + "/adferror/?errmsg=Error in function ADFBannerUtils.getBrowser " + e.message;*/}catch(e){}};
};

Adform.ADFBannerUtils.prototype.setBannerRegisteredStatus = function(bannerId){
    try{
        this.addBannerAttribute(bannerId, "registered", 1);
        if(typeof Adform.ADFEventsInstance != "undefined"){
            if(Adform.ADFEventsInstance != null){
                Adform.ADFEventsInstance.register(this.banners[bannerId]);
            }
        }
    } catch(e){try{/*new Image().src = Adform.host + "/adferror/?errmsg=Error in function ADFBannerUtils.setBannerRegisteredStatus " + e.message;*/}catch(e){}};
};

Adform.ADFBanner = function(){
    try{
        var OOBClickTrack = "";
        var URL = "";
        var CREFURL = "";
        if(!Adform.ADFBannerParams){
            URL = Adform.ADFBannerData.URL;
            CREFURL = Adform.ADFBannerData.CREFURL;
        } else {
            var params = Adform.ADFBannerParams.shift();
            URL = params.URL;
            CREFURL = params.CREFURL;
        }
        typeof Adform.ADFIframe == "undefined"?this.iframeMode=0:this.iframeMode=1;
        this.utilsInstance = Adform.ADFBannerUtils.getInstance();
        var tagID = this.utilsInstance.getTagID();
        this.utilsInstance.addNewBanner(tagID, this.iframeMode); 
        if(URL.indexOf("OOBClickTrack=") !=-1){
            OOBClickTrack= URL.split(";OOBClickTrack=")[1];
            if(OOBClickTrack != null){ OOBClickTrack = encodeURIComponent(OOBClickTrack); }
            URL = URL.split(";OOBClickTrack=")[0];
            this.utilsInstance.addBannerAttribute(tagID, "msn", 1);
        };       
        document.write('<scr'+'ipt type="text/javascript" src="'+URL+';adfxid='+tagID+';'+Math.floor(Math.random()*11000)+';set1='+this.utilsInstance.getSet1()+';set2='+this.utilsInstance.getSet2()+(OOBClickTrack!=""?';OOBClickTrack='+OOBClickTrack:"")+'&CREFURL='+CREFURL+'"></scr'+'ipt>');      
    } catch(e){/*new Image().src = Adform.host + "/adferror/?errmsg=Error in function ADFBanner " + e.toString();*/};
};
new Adform.ADFBanner();
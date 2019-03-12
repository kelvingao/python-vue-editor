<template>
  <div class="ace-container">
    <div id="content">
      <!-- ************  CODING ZONE  ************ -->
      <div id="code">
          <form method="post" >
              <div id="title-code" class="head-section">
                Source Code
              </div>

              <input id="launch-button" class="head-section" type="submit" value="Launch" />

              <!-- <textarea id="text-code" name="code" rows=18 cols=70>
                {{ code }}
              </textarea><br/> -->

              <div id="text-code-ace" ref="ace">{{ code }}</div>
          </form>
      </div>
      
      <!-- ************ RUNNING ZONE RESULTS ************ -->
      
      <div id="result">
          <div id="title-result" class="head-section">
              Output result
          </div>
          <textarea id="text-result" rows="18" cols="70" readonly></textarea>
      </div>
      
      <!-- ************ COMPILATION RESULTS ZONE ************ -->
      
      <div id="compile">
          <div id="title-compile" class="head-section">
              Compilation / Output
          </div>
          <textarea id="text-compile" rows="7" cols="140" readonly></textarea>
      </div>
    </div>
  </div>
</template>

<script>
  import ace from 'ace-builds'
  import 'ace-builds/webpack-resolver' // 在 webpack 环境中使用必须要导入

 
  export default {
    name:'AceContainer',

    data () {
      return {
        code: 'import sys\n\
import os\n\n\
if __name__ == "__main__":\n\
    print "Hello Python World!!',
        ace: null,
        themePath: 'ace/theme/tomorrow', // 不导入 webpack-resolver，该模块路径会报错
        modePath: 'ace/mode/python' // 同上
      }
    },

    mounted () {
      this.ace = ace.edit("text-code-ace", {
        maxLines: 20, // 最大行数，超过会自动出现滚动条
        minLines: 16, // 最小行数，还未到最大行数时，编辑器会自动伸缩大小
        fontSize: 14, // 编辑器内字体大小
        theme: this.themePath, // 默认设置的主题
        mode: this.modePath, // 默认设置的语言模式
        tabSize: 4 // 制表符设置为 4 个空格大小
      })
    },
    
    
  }
</script>
<style>
li {
    display: inline;
}

#content {
    position: absolute;
    top: 50px;
    min-height: 600px;
    min-width: 900px;
    width: 100%;
    height: 90%;
}

#code {
    position: absolute;
    height: 60%;
    min-height: 350px;
    min-width: 400px;
    left: 10px;
    top: 5px;
    width: 48%;
}

#result {
    position: absolute;
    height: 60%;
    min-height: 350px;
    min-width: 400px;
    right: 10px;
    top: 5px;
    width: 48%;
}

#compile {
    position: absolute;
    right: 10px;
    left: 10px;
    min-height: 100px;
    min-width: 400px;
    /*width: 100%;*/
    height: 40%;
    bottom: 0px;
}

#launch-button {
    position: absolute;
    right: 0px;
}

.head-section {
    position: absolute;
    top: 0px;
    font-weight:bold;
}

#title-code {
    position: absolute;
    left: 5px;
}

#title-result {
    position: absolute;
    left: 5px;
}

#title-compile{
    position: absolute;
    left: 5px;
}

#text-code, #text-code-ace {
    position: absolute;
    top: 50px;
    width: 100%;
    height: 80%;
}

#text-code-ace {
    padding: 2px;
    border: 1px solid rgb(169, 169, 169);
}

#text-result {
    position: absolute;
    top: 50px;
    width: 100%;
    height: 80%;
}

#text-compile {
    position: absolute;
    bottom: 0px;
    left: 5px;
    width: 98%;
    height: 80%;
}

.hidden {
    display: none;
}
</style>


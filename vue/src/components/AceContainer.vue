<template>
  <div class="ace-container">
    <div id="content">
      <!-- CODING ZONE -->
      <div id="code">
        <div id="title-code" class="head-section">
          Source Code
        </div>

        <!-- <input id="launch-button" class="head-section" type="submit" value="Launch" /> -->
        <button id="launch-button" class="head-section" v-on:click='launch'>Launch</button>

        <div id="text-code">
          <editor v-model="code" @init="editorInit" lang="python" theme="chrome" ref="ace"></editor>
        </div>
      </div>

      <!-- RUNNING ZONE RESULTS -->
      <div id="result">
          <div id="title-result" class="head-section">
              Output result
          </div>
          <textarea v-model="output" id="text-result" rows="18" cols="70" readonly></textarea>
      </div>

      <!-- COMPILATION RESULTS ZONE  -->
      <div id="compile">
          <div id="title-compile" class="head-section">
              Compilation / Output
          </div>
          <textarea v-model="compil" id="text-compile" rows="7" cols="140" readonly></textarea>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name:'AceContainer',

  components: {
        editor: require('vue2-ace-editor'),
  },

  data() {
    return {
      code:'',
      output:'',
      compil:''
    }
  },
  
  methods: {
      editorInit: function () {
          require('brace/ext/language_tools')
          require('brace/mode/python')                
          require('brace/theme/chrome')
      },
      launch(event) {
        axios.post('http://localhost:5000/runpy', this.code, {
          headers: { 'Content-Type': 'text/plain' }
        })
          .then(response => {
            this.output = response.data.output
            this.compil = response.data.compil
          })
      }
  },

  mounted() {
        axios.get('http://localhost:5000/')
          .then(response => {
            this.code = response.data.code
            this.output = response.data.output
            this.compil = response.data.compil
          })      
  }

}
</script>

<style>
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

</style>
## Talk with 3x Board Personas 

At the same time

{{chatbot   name             = "Main Chat bot" 
            initial_message  = "Hi, Ask a question here and see the answer in multiple LLMs" 
            initial_prompt   = "Hi, I'm the CISO and would like time on the board agenda to discuss the latest cyber security threats"
            edit_mode        = "false"
            platform         = "Groq (Free)"
            provider         = "Meta"
            model            = "llama3-70b-8192"
            channel          = "root-llm"
}}
<div class="row">
    <div class="col-4">
        {{chatbot   name               = "Board Member #1 (no patience)"  
                    system_prompt      = "Act like are a board member that has legal responsibilities for the company | Reply in one paragraph only | no experience in CyberSecurity | you have no patience for technical details and want really actionable data "
                    show_sent_messages = "false"
                    edit_mode          = "false" 
                    platform           = "Groq (Free)"
                    provider           = "Meta"
                    model              = "llama3-70b-8192"
                    channel            = "shared-llm-es" 
        }}
    </div>
    <div class="col-4">
        {{chatbot   name               = "Board Member #2 (Hired CISO)"  
                    system_prompt      = "Act like are a board member that has legal responsibilities for the company | Reply in one paragraph only | some experience in CyberSecurity  | you helped to hired the CISO and always try to coach her to be more business oriented"
                    show_sent_messages = "false"
                    edit_mode          = "false" 
                    platform           = "Groq (Free)"
                    provider           = "Meta"
                    model              = "llama3-70b-8192"
                    channel            = "shared-llm-pt" 
        }}
    </div>
    <div class="col-4">
        {{chatbot   name               = "Board Member #3 - (Jaded and Sarcastic)"  
                    system_prompt      = "Act like are a board member that has legal responsibilities for the company | Reply in one paragraph only | no experience in CyberSecurity    | you are highly sarcastic, are jaded with CyberSecurity and you really do not like the Board Member who hired the CISO"
                    show_sent_messages = "false"
                    edit_mode          = "false" 
                    platform           = "Groq (Free)"
                    provider           = "Meta"
                    model              = "llama3-70b-8192"
                    channel            = "shared-llm-fr" 
        }}
    </div>
</div>

<script type="module" src="/web_components/js/chat-bots/Chatbot_OpenAI.mjs"></script>
<script src="/assets/plugins/marked/marked.min.js"></script>

import streamlit as st

# Define the HTML code for the full-page Flowise chatbot with custom styles
flowise_html = """
<flowise-fullchatbot></flowise-fullchatbot>
<script type="module">
    import Chatbot from "https://cdn.jsdelivr.net/npm/flowise-embed/dist/web.js";
    Chatbot.initFull({
        chatflowid: "0b815c16-cfc0-41d9-91ce-d5bd9cb76d89",
        apiHost: "https://flowise-yvjw.onrender.com",
        theme: {
            chatWindow: {
                showTitle: true,
                title: 'Toll Solutions and Case Study Email Writer',
                titleAvatarSrc: '',
                showAgentMessages: true,
                welcomeMessage: 'Hello! Who are we writing an email to today?',
                errorMessage: 'This is a custom error message',
                backgroundColor: "#ffffff",
                height: 700,
                width: '100%',
                fontSize: 16,
                poweredByTextColor: "#000000",
                botMessage: {
                    backgroundColor: "#f4f4f4",
                    textColor: "#000000",
                    showAvatar: true,
                    avatarSrc: "https://cdn-icons-png.flaticon.com/512/2021/2021646.png",
                },
                userMessage: {
                    backgroundColor: "#007a68",
                    textColor: "#ffffff",
                    showAvatar: true,
                    avatarSrc: "https://raw.githubusercontent.com/zahidkhawaja/langchain-chat-nextjs/main/public/usericon.png",
                },
                textInput: {
                    placeholder: 'Type your question here...',
                    backgroundColor: '#ffffff',
                    textColor: '#303235',
                    sendButtonColor: '#007a68',
                    maxChars: 50,
                    maxCharsWarningMessage: 'You have exceeded the character limit.',
                    autoFocus: true,
                    sendMessageSound: true,
                    receiveMessageSound: true,
                },
                feedback: {
                    color: '#303235',
                },
                footer: {
                    textColor: '#303235',
                    text: 'Made by',
                    company: 'Capgemini',
                    companyLink: 'https://capgemini.com',
                }
            },
            button: {
                backgroundColor: "#007a68",
                right: 20,
                bottom: 20,
                size: 48, // small | medium | large | number
                dragAndDrop: true,
                iconColor: "white",
                customIconSrc: "",
            },
            tooltip: {
                showTooltip: true,
                tooltipMessage: 'Hi There 👋!',
                tooltipBackgroundColor: 'black',
                tooltipTextColor: 'white',
                tooltipFontSize: 16,
            }
        }
    });
</script>
"""

# Embed the logo and title next to each other using a flexbox
st.markdown(
    """
    <div style="display: flex; align-items: center; margin-bottom: 40px;">
        <img src="https://cms.tollgroup.com/sites/default/files/2022-09/toll-logo.svg" alt="Toll Logo" style="height: 60px; margin-right: 20px;">
        <div>
            <p style="margin-top: 0;">Helps write emails for Account Managers with solutions and case studies.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Embed the full-page Flowise chatbot in Streamlit
st.components.v1.html(flowise_html, height=800)
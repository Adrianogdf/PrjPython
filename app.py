import streamlit as st
from datetime import datetime, time #Necessário para fazer concatenação de data hora.


def main():


    st.title("sistema de CRM e Vendas da ZapFlow - FrontEnd Simples")
    email = st.text_input("Campo de texto para inserção do email do vendedor")
    data = st.date_input("Data da Compra", datetime.now())
    hora = st.time_input("Hora da Compra", value=time(9, 0)) # valor padrão: 09:00
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de produtos", min_value=1, step=1)
    produto = st.selectbox("Produto", options=["ZapFlow com Gemini","ZapFlow com ChatGpt","ZapFlow com Llama3.0"])

    if st.button("Salvar"):

        data_hora = datetime.combine(data, hora)
        st.write("**Dados da Venda:**")
        st.write(f"Email do Vendedor:{email}")
        st.write(f"Data e Hora da Compra:{data_hora}")
        st.write(f"Valor da Venda: R$ {valor:.2f}")
        st.write(f"Quantidade de Produto: {quantidade}")
        st.write(f"Produto: {produto}")

#Só executar quando eu rodar este script
if __name__ == "__main__":
    main()


flowchart LR
    %% =============================
    %%   HEADER / STAGES
    %% =============================
    subgraph Pipeline ["📦 RDTrackR Architecture Pipeline"]
        direction LR
        P1["Process Data"]
        P2["Application Logic (.NET 8)"]
        P3["Deploy"]
        P4["Monitor"]
    end

    P1 --- P2 --- P3 --- P4

    %% =============================
    %% PROCESS DATA SECTION
    %% =============================
    subgraph PD["⚙️ Processamento de Dados"]
        direction TB
        STOCK["
            📦 Stock Items  
            - Quantidade  
            - Reorder Point  
            - Warehouse  
        "]

        MOVEMENT["
            🔄 Movements  
            - Entrada / Saída  
            - Origem / Destino  
            - Auditoria  
        "]

        SUPPLIERS["
            👤 Suppliers  
            - Cadastro  
            - Fornecedores  
            - Histórico  
        "]
    end

    %% =============================
    %% CORE .NET BACKEND
    %% =============================
    subgraph CORE["🟪 Backend .NET 8 (Domain + Application + Infrastructure)"]
        direction TB
        
        API["
            🔌 RDTrackR API  
            Endpoint HTTPS  
            Autenticação JWT  
            Swagger (OpenAPI)  
        "]

        SIGNALR["
            📡 SignalR Hub  
            Notificações em tempo real  
        "]

        SERVICES["
            🧠 Application UseCases  
            - Movement  
            - Products  
            - Warehouse  
            - Reports  
        "]
    end

    %% relations
    PD --> CORE
    CORE --> SIGNALR

    %% =============================
    %% DATABASE
    %% =============================
    SQL["
        🗄️ SQL Server  
        - Produtos  
        - Pedidos de Compra  
        - Movimentações  
        - Auditoria  
    "]

    CORE --> SQL

    %% =============================
    %% FRONTEND
    %% =============================
    subgraph FRONT["💠 Frontend React + Vite + Tailwind"]
        REACT_UI["
            🖥️ Web UI  
            - Dashboard  
            - Movimentações  
            - Relatórios  
        "]

        REALTIME["⚡ Live Updates (SignalR)"]
    end

    CORE --> REACT_UI
    SIGNALR --> REALTIME
    REALTIME --> REACT_UI

    %% =============================
    %% DEPLOYMENT
    %% =============================
    subgraph DEPLOYMENT["🚀 Deploy (Docker + GitHub Actions)"]
        DOCKER["
            🐳 Docker / Docker Compose  
            - API  
            - Frontend  
            - SQL Server  
        "]

        GHA["
            🔁 GitHub Actions  
            - CI / CD  
            - SonarCloud  
            - Testes  
        "]
    end

    P3 --> DOCKER
    P3 --> GHA

    %% =============================
    %% MONITOR SECTION
    %% =============================
    subgraph MONITORING["📊 Monitoramento"]
        LOGS["
            📝 Logs Estruturados  
            - Serilog (futuro)  
            - CloudWatch (AWS futuro)  
        "]

        HEALTHCHECK["
            💓 Health Checks  
            /health  
        "]
    end

    DEPLOYMENT --> MONITORING
    MONITORING --> P4

    %% =============================
    %% PUBLIC ACCESS
    %% =============================
    URL["🌐 https://rdtrackr.com.br"]
    REACT_UI --> URL

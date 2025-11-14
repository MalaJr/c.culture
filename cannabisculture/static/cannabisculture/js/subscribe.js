$(document).ready(function() {
    $("#newsletter-form").on("submit", function(e) {
        e.preventDefault();

        const email = $("input[name='email']").val();
        const csrfToken = $("input[name='csrfmiddlewaretoken']").val();

        $.ajax({
            url: "/salvar-email/",
            type: "POST",
            data: {
                email: email,
                csrfmiddlewaretoken: csrfToken
            },
            success: function(response) {
                const header = $("header");
                const headerText = $(".text-header h4");

                // Define cores e brilho
                let bgColor = response.status === "ok" ? "#32CD32" : "#E3DC27";
                let glow = response.status === "ok" 
                    ? "0 0 25px 5px rgba(50,205,50, 0.6)" 
                    : "0 0 25px 5px rgba(227, 220, 39, 0.6)";

                // Fade out do texto
                headerText.fadeOut(300, function() {
                    header.css({
                        "background-color": bgColor,
                        "box-shadow": glow
                    });

                    if (response.status === "ok") {
                        headerText.css("color", "white");
                    } else {
                        headerText.css("color", "black"); // texto preto no alerta amarelo
                    }

                    headerText.text(response.mensagem);
                    headerText.fadeIn(400);
                });

                // Remove o efeito e volta ao padrão após 5 segundos
                setTimeout(function() {
                    headerText.fadeOut(300, function() {
                        header.css({
                            "background-color": "#2e7d32",
                            "box-shadow": "none"
                        });
                        headerText.css("color", "white");
                        headerText.text("Bem-Vindo(a) ao portal!");
                        headerText.fadeIn(400);
                    });
                }, 3500);
            },
            error: function() {
                const header = $("header");
                const headerText = $(".text-header h4");

                headerText.fadeOut(300, function() {
                    header.css({
                        "background-color": "#E3DC27",
                        "box-shadow": "0 0 25px 5px rgba(227, 220, 39, 0.6)"
                        
                    });
                    headerText.css("color", "black");
                    headerText.text("Erro no servidor. Tente novamente.");
                    headerText.fadeIn(400);
                });

                setTimeout(function() {
                    headerText.fadeOut(300, function() {
                        header.css({
                            "background-color": "#2e7d32",
                            "box-shadow": "none"
                        });
                        headerText.css("color", "white");
                        headerText.text("Bem-Vindo(a) ao portal!");
                        headerText.fadeIn(400);
                    });
                }, 3500);
            }
        });
    });
});

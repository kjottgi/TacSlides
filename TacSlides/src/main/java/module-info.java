module tactic.tacslides {
    requires javafx.controls;
    requires javafx.fxml;


    opens tactic.tacslides to javafx.fxml;
    exports tactic.tacslides;
}
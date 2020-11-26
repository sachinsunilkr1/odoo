odoo.define("website_clear_cart", function(require) {
    "use strict";
    var ajax = require("web.ajax");

            $(document).ready(function(){
                $(".oe_website_sale").each(function() {
                    var oe_website_sale = this;

                    $(oe_website_sale).on("click", ".oe_cart #clear_cart_button", function() {
                        ajax.jsonRpc("/shop/clear_cart", "call", {}).then(function() {
                            location.reload();
                        });
                        return false;
                    });
                });
            });
});
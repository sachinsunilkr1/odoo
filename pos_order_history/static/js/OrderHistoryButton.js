odoo.define('pos_order_history.OrderHistoryButton', function(require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const { useListener } = require('web.custom_hooks');
    const Registries = require('point_of_sale.Registries');
    const { posbus } = require('point_of_sale.utils');
    var rpc = require('web.rpc');



    class OrderHistoryButton extends PosComponent {
        constructor() {
                super(...arguments);
                useListener('click', this.onClick);

            }
        onClick() {

            this.showScreen('OrderHistoryScreen');
            var orders = [];

            orders = rpc.query({
                            model: 'pos.order',
                            method: 'search_read',
                            args: [[], ['name','partner_id','session_id','pos_reference','date_order','amount_total']],
                            }).then(function (orders) {

                            console.log(orders);

                       });

        console.log("order",orders);

        return orders;

        }


//        get count() {
//            if (this.env.pos) {
//                return this.env.pos.get_order_list().length;
//            } else {
//                return 0;
//            }
//        }

        }
        OrderHistoryButton.template = 'HistoryButton';
        ProductScreen.addControlButton({
        component : OrderHistoryButton,
        condition : function(){
            return this.env.pos
            },

    })

        Registries.Component.add(OrderHistoryButton);
        return OrderHistoryButton;


});

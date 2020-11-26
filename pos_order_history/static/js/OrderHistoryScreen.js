odoo.define('point_of_sale.OrderHistoryScreen', function (require) {
    'use strict';

    const Registries = require('point_of_sale.Registries');
    const IndependentToOrderScreen = require('point_of_sale.IndependentToOrderScreen');
    const { useListener } = require('web.custom_hooks');
    const { posbus } = require('point_of_sale.utils');



    class OrderHistoryScreen extends IndependentToOrderScreen {
        constructor() {
            super(...arguments);

        }
       get all_order(){
        console.log("abc");
         return this
        }
//            var orders = [];
//
//
//            var orders = rpc.query({
//                            model: 'pos.order',
//                            method: 'search_read',
//                            args: [[], ['partner_id','session_id','date_order']],
//                            }).then(function (partner_id) {
//                            console.log(partner_id);
//
//                              orders.push(new exports.Order({},{
//                        pos: this,
//                        json: order,
//                                    }));
//
//
//
//                       });
//
//        return orders;





//return this.env.pos._load_orders();


//
//        _setOrder(order) {
//            this.env.pos.set_order(order);
//        }
//
//        getDate(order) {
//            return moment(order.creation_date).format('YYYY-MM-DD hh:mm A');
//        }
//        getTotal(order) {
//            return this.env.pos.format_currency(order.get_total_with_tax());
//        }
//        getCustomer(order) {
//            return order.get_client_name();
//        }
//        getCardholderName(order) {
//            return order.get_cardholder_name();
//        }
//        getEmployee(order) {
//            return order.employee.name;
//        }





    }
    OrderHistoryScreen.template = 'OrderHistoryScreen';

    Registries.Component.add(OrderHistoryScreen);

    return OrderHistoryScreen;
});
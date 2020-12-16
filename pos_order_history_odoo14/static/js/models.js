//odoo.define('pos_order_history.models', function (require) {
//  "use strict";
//  var rpc = require('web.rpc');
//
//  orderList: function () {
//        var self = this;
//        return rpc.query({
//                    model: 'pos.order',
//                    method: 'search_read',
//                    args: [[], ['partner_id','session_id','date_order']],
//                    }).then(function (partner_id) {
//                        console.log(partner_id); });
//
//
//        },
//  return orderList;
//
//
//        });
//
//
//
////
////    var models = require('point_of_sale.models');
////    var rpc = require('web.rpc');
////
////    var order_list = rpc.query({
////                    model: 'pos.order',
////                    method: 'search_read',
////                    args: [[], ['partner_id','session_id','date_order']],
////                }).then(function (partner_id) {
////                console.log(partner_id); });
////  get_all_order: function(){
////        return this.self.pos_orders
////    },
////
////  return orders_list
////
////
////
////});

odoo.define('pos_order_history.OrderHistoryScreen', function (require) {
    'use strict';

    const Registries = require('point_of_sale.Registries');
    const IndependentToOrderScreen = require('point_of_sale.IndependentToOrderScreen');
    const { useListener } = require('web.custom_hooks');
    const { posbus } = require('point_of_sale.utils');
    var rpc = require('web.rpc');
    var models = require('point_of_sale.models');
    var PosModelSuper = models.PosModel;
    const ProductScreen = require('point_of_sale.ProductScreen');

//Loads Moadel into pos
 models.load_models({
            model: 'pos.order',
            fields: ['id', 'name', 'session_id', 'state', 'pos_reference', 'partner_id', 'amount_total','lines', 'amount_tax','sequence_number', 'fiscal_position_id', 'pricelist_id', 'create_date'],
            domain: function(self){ return [['company_id','=',self.company.id]]; },
            loaded: function (self, pos_orders) {
            var orders = [];
            for (var i in pos_orders){
                orders[pos_orders[i].id] = pos_orders[i];


            }
            self.pos_orders = orders;
            self.order = [];
            for (var i in pos_orders){
                self.order[i] = pos_orders[i];

            }


        },

    });
//Model extending for new order to display in the pos
models.PosModel = models.PosModel.extend({
  _save_to_server: function (orders, options) {
   var result_new = PosModelSuper.prototype._save_to_server.call(this, orders, options);
   var self = this;
   var new_order = {};
   var orders_list = self.pos_orders;
    for (var i in orders) {
      var partners = self.partners;

      var partner = "";
      for(var j in partners){
           if(partners[j].id == orders[i].data.partner_id){
                partner = partners[j].name;
             }
         }
            new_order = {
                'amount_tax': orders[i].data.amount_tax,
                'amount_total': orders[i].data.amount_total,
                'pos_reference': orders[i].data.name,
                'partner_id': [orders[i].data.partner_id, partner],
                'session_id': [self.pos_session.id, self.pos_session.name]
            };
            orders_list.push(new_order);
            self.pos_orders = orders_list;

        }
        return result_new;
    },
});

//Define the Order History Screen

class OrderHistoryScreen extends IndependentToOrderScreen {
          constructor() {
            super(...arguments);
            useListener('close-screen', this.close);
        }
// getter for passing the order list to qweb
        get filteredOrderList() {
            return this.env.pos.order;
        }
// getter for passing the selected client id to the qweb
        get SelectedClient(){
        return this.env.pos.attributes.selectedClient.id
        }
// getter for passing the selected client id to the qweb
        get SelectedClientName(){
            if( this.env.pos.attributes.selectedClient==null){
            return 0;
            }

        }
    }

    OrderHistoryScreen.template = 'OrderHistoryScreen';

    Registries.Component.add(OrderHistoryScreen);

    return OrderHistoryScreen;
});

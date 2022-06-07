/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.tinkertech.admin;

import java.math.BigInteger;
import java.security.MessageDigest;

class Hash {
    
        String getSHA256(String data){

            try {

                MessageDigest md = MessageDigest.getInstance("SHA-256");
                BigInteger number = new BigInteger(1, md.digest(data.getBytes("UTF-8")));
                StringBuilder hexStr = new StringBuilder(number.toString(16));

                while (hexStr.length() < 32) {
                    hexStr.insert(0, '0');
                }
                return hexStr.toString();
            }catch (Exception e){
                return null;
            }
    }
}

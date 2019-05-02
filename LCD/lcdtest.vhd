library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;
---- Uncomment the following library declaration if instantiating
---- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;
entity lcdtest is
	port(
		clk, reset : in std_logic;
		SF_D : out std_logic_vector(3 downto 0);
		LCD_E, LCD_RS, LCD_RW, SF_CE0 : out std_logic;
		LED : out std_logic_vector(7 downto 0) );
end lcdtest;

architecture Behavioral of lcdtest is
	type tx_sequence is (high_setup, high_hold, oneus, low_setup, low_hold, fortyus, done);
	signal tx_state : tx_sequence := done;
	signal tx_byte : std_logic_vector(7 downto 0);
	signal tx_init : std_logic := '0';
	type init_sequence is (idle, fifteenms, one, two, three, four, five, six, seven, eight, done);
	signal init_state : init_sequence := idle;
	signal init_init, init_done : std_logic := '0';
	signal i : integer range 0 to 750000 := 0;
	signal i2 : integer range 0 to 2000 := 0;
	signal i3 : integer range 0 to 82000 := 0;
	signal sekunde : integer range 0 to 100000000 := 0;
	signal sec_changed : std_logic;
	signal last_sec : std_logic;
	signal first_time : integer range 0 to 1 := 0;
	signal SF_D0, SF_D1 : std_logic_vector(3 downto 0);
	signal LCD_E0, LCD_E1 : std_logic;
	signal mux : std_logic;
	signal c1, c2, c4, c5, c6, c7, c8 : std_logic_vector(7 downto 0);
	type display_state is (init, function_set, entry_set, set_display, clr_display, pause, set_addr, char_1, char_2, char_3,
	char_4, char_5, char_6, char_7, char_8, wait_second);
	signal cur_state : display_state := init;
begin
	LED <= "00000000"; --tx_byte; --for diagnostic purposes
	SF_CE0 <= '1'; --disable intel strataflash
	LCD_RW <= '0'; --write only
	--The following "with" statements simplify the process of adding and removing states.
	--when to transmit a command/data and when not to
	with cur_state select
		tx_init <= '0' when init | pause | wait_second,
		           '1' when others;

	--control the bus
	with cur_state select
		mux <= '1' when init,
				 '0' when others;
	--control the initialization sequence
	with cur_state select
		init_init <= '1' when init,
						 '0' when others;

	--register select
	with cur_state select
		LCD_RS <= '0' when function_set|entry_set|set_display|clr_display|set_addr,
					 '1' when others;
	--what byte to transmit to lcd
	--refer to datasheet for an explanation of these values
	with cur_state select
		tx_byte <= "00101000" when function_set,
					  "00000110" when entry_set,
					  "00001100" when set_display,
					  "00000001" when clr_display,
					  "10000000" when set_addr,
								 c1 when char_1,			-- prva cifra sata (menja se)
								 c2 when char_2,			-- druga cifra sata (menja se)
					  "00111010" when char_3,			-- dvotacka (ne menja se)
								 c4 when char_4,			-- prva cifra minuta (menja se)
								 c5 when char_5,			-- druga cifra minuta (menja se)
					  "00111010" when char_6,			-- dvotacka (ne menja se)
								 c7 when char_7,			-- prva cifra sekunde (menja se)
								 c8 when char_8,			-- druga cifra sekunde (menja se)
					  "00000000" when others;
					  
	sat : process(clk, reset)
	begin
	-- pocetna inicijalizacija cifara sata
		if (reset = '1') then
			c1 <= "00110000";
			c2 <= "00110000";
			c4 <= "00110000";
			c5 <= "00110000";
			c7 <= "00110000";
			c8 <= "00110000";
			sekunde <= 0;
		elsif (rising_edge(clk)) then
			if (first_time = 0) then
		-- pocinjemo od 23:59:55 da bismo testirali prelaze sati, minuta, sekundi
				c1 <= "00110010";
				c2 <= "00110011";
				c4 <= "00110101";
				c5 <= "00111001";
				c7 <= "00110101";
				c8 <= "00110101";
				first_time <= 1;
				sec_changed <= '0';
			end if;
			
		-- mehanizam funkcionisanja sata
		-- c7c8 sekunde
		-- c4c5 minuti
		-- c1c2 sati
			sekunde <= sekunde + 1;
			if (sekunde = 50000000) then
				sekunde <= 0;
				sec_changed <= not(sec_changed);			-- sekunda je prosla, potrebno za okidanje za displej
				if (c8 = "00111001") then
					c8 <= "00110000";
					c7 <= c7 + "00000001";
					if (c7 = "00110101") then
						c7 <= "00110000";
						c5 <= c5 + "00000001";
						if (c5 = "00111001") then
							c5 <= "00110000";
							c4 <= c4 + "00000001";
							if (c4 = "00110101") then
								c4 <= "00110000";
								c2 <= c2 + "00000001";
								if (c1 < "00110010") then
									if (c2 = "00111001") then
										c2 <= "00110000";
										c1 <= c1 + "00000001";
									end if;
								else
									if (c2 = "00110011") then
										c2 <= "00110000";
										c1 <= "00110000";
									end if;
								end if;
							end if;
						end if;
					end if;
				else
					c8 <= c8 + "00000001";				-- sekunda je prosla
				end if;
			end if;
		end if;
	end process sat;

	--main state machine
	display: process(clk, reset)
	begin
		if(reset='1') then
			cur_state <= function_set;
		elsif(clk='1' and clk'event) then
		case cur_state is
			--refer to intialize state machine below
		when init =>
			if(init_done = '1') then
				cur_state <= function_set;
				last_sec <= '0';
			else
				cur_state <= init;
			end if;
		--every other state but pause uses the transmit state machine
		when function_set =>
			if(i2 = 2000) then
				cur_state <= entry_set;
			else
				cur_state <= function_set;
			end if;
		when entry_set =>
			if(i2 = 2000) then
				cur_state <= set_display;
			else
				cur_state <= entry_set;
			end if;
		when set_display =>
			if(i2 = 2000) then
				cur_state <= clr_display;
			else
				cur_state <= set_display;
			end if;
		when clr_display =>
			i3 <= 0;
			if(i2 = 2000) then
				cur_state <= pause;
			else
				cur_state <= clr_display;
			end if;
		when pause =>
			if(i3 = 82000) then
				cur_state <= set_addr;
				i3 <= 0;
			else
				cur_state <= pause;
				i3 <= i3 + 1;
			end if;
		when set_addr =>
			if(i2 = 2000) then
				cur_state <= char_1;
			else
				cur_state <= set_addr;
			end if;
			
		-- char su karakteri za ispis na LCD displeju
		when char_1 =>
			if(i2 = 2000) then
				cur_state <= char_2;
			else
				cur_state <= char_1;
			end if;
		when char_2 =>
			if(i2 = 2000) then
				cur_state <= char_3;
			else
				cur_state <= char_2;
			end if;
		when char_3 =>
			if(i2 = 2000) then
				cur_state <= char_4;
			else
				cur_state <= char_3;
			end if;
		when char_4 =>
			if(i2 = 2000) then
				cur_state <= char_5;
			else
				cur_state <= char_4;
			end if;
		when char_5 =>
			if(i2 = 2000) then
				cur_state <= char_6;
			else
				cur_state <= char_5;
			end if;
		when char_6 =>
			if(i2 = 2000) then
				cur_state <= char_7;
			else
				cur_state <= char_6;
			end if;
		when char_7 =>
			if(i2 = 2000) then
				cur_state <= char_8;
			else
				cur_state <= char_7;
			end if;
		when char_8 =>
			if(i2 = 2000) then
				cur_state <= wait_second;
			else
				cur_state <= char_8;
			end if;
		
		-- ceka sekundu pre ponovnog ispisivanja ekrana 
		-- (sec_changed se menja u procesu "sat" i na ovaj nacin okida promene na displeju)
		when wait_second =>
			if (not(sec_changed = last_sec)) then
				cur_state <= set_display;
				last_sec <= sec_changed;
			else
				cur_state <= wait_second;
			end if;
			
		end case;
		end if;
end process display;

with mux select
	SF_D <= SF_D0 when '0', --transmit
	SF_D1 when others; --initialize

with mux select
	LCD_E <= LCD_E0 when '0', --transmit
	LCD_E1 when others; --initialize

--specified by datasheet
transmit : process(clk, reset, tx_init)
begin
	if(reset='1') then
		tx_state <= done;
	elsif(clk='1' and clk'event) then
		case tx_state is
			when high_setup => --40ns
				LCD_E0 <= '0';
				SF_D0 <= tx_byte(7 downto 4);
				if(i2 = 2) then
					tx_state <= high_hold;
					i2 <= 0;
				else
					tx_state <= high_setup;

					i2 <= i2 + 1;
				end if;
			when high_hold => --230ns
				LCD_E0 <= '1';
				SF_D0 <= tx_byte(7 downto 4);
				if(i2 = 12) then
					tx_state <= oneus;
					i2 <= 0;
				else
					tx_state <= high_hold;
					i2 <= i2 + 1;
				end if;
			when oneus =>
				LCD_E0 <= '0';
				if(i2 = 50) then
					tx_state <= low_setup;
					i2 <= 0;
				else
					tx_state <= oneus;
					i2 <= i2 + 1;
				end if;
			when low_setup =>
				LCD_E0 <= '0';
				SF_D0 <= tx_byte(3 downto 0);
				if(i2 = 2) then
					tx_state <= low_hold;
					i2 <= 0;
				else
					tx_state <= low_setup;
					i2 <= i2 + 1;
				end if;
			when low_hold =>
				LCD_E0 <= '1';
				SF_D0 <= tx_byte(3 downto 0);
				if(i2 = 12) then
					tx_state <= fortyus;
					i2 <= 0;
				else
					tx_state <= low_hold;
					i2 <= i2 + 1;
				end if;
			when fortyus =>
				LCD_E0 <= '0';
				if(i2 = 2000) then
					tx_state <= done;
					i2 <= 0;
				else
					tx_state <= fortyus;
					i2 <= i2 + 1;
				end if;
			when done =>
				LCD_E0 <= '0';
				if(tx_init = '1') then
					tx_state <= high_setup;
					i2 <= 0;
				else
					tx_state <= done;
					i2 <= 0;
				end if;

		end case;
	end if;
end process transmit;

--specified by datasheet
power_on_initialize: process(clk, reset, init_init) --power on initialization sequence
begin
	if(reset='1') then
		init_state <= idle;
		init_done <= '0';
	elsif(clk='1' and clk'event) then
		case init_state is
			when idle =>
				init_done <= '0';
				if(init_init = '1') then
					init_state <= fifteenms;
					i <= 0;
				else
					init_state <= idle;
					i <= i + 1;
				end if;
			when fifteenms =>
				init_done <= '0';
				if(i = 750000) then
					init_state <= one;
					i <= 0;
				else
					init_state <= fifteenms;
					i <= i + 1;
				end if;
			when one =>
				SF_D1 <= "0011";
				LCD_E1 <= '1';
				init_done <= '0';
				if(i = 11) then
					init_state<=two;
					i <= 0;
				else
					init_state<=one;
					i <= i + 1;
				end if;
			when two =>
				LCD_E1 <= '0';
				init_done <= '0';
				if(i = 205000) then
					init_state<=three;
					i <= 0;
				else
					init_state<=two;
					i <= i + 1;
				end if;
			when three =>
				SF_D1 <= "0011";
				LCD_E1 <= '1';
				init_done <= '0';
				if(i = 11) then
					init_state<=four;
					i <= 0;
				else
					init_state<=three;
					i <= i + 1;
				end if;
			when four =>
				LCD_E1 <= '0';
				init_done <= '0';
				if(i = 5000) then
					init_state<=five;

					i <= 0;
				else
					init_state<=four;
					i <= i + 1;
				end if;
			when five =>
				SF_D1 <= "0011";
				LCD_E1 <= '1';
				init_done <= '0';
				if(i = 11) then
					init_state<=six;
					i <= 0;
				else
					init_state<=five;
					i <= i + 1;
				end if;
			when six =>
				LCD_E1 <= '0';
				init_done <= '0';
				if(i = 2000) then
					init_state<=seven;
					i <= 0;
				else
					init_state<=six;
					i <= i + 1;
				end if;
			when seven =>
				SF_D1 <= "0010";
				LCD_E1 <= '1';
				init_done <= '0';
				if(i = 11) then
					init_state<=eight;
					i <= 0;
				else
					init_state<=seven;
					i <= i + 1;
				end if;
			when eight =>
				LCD_E1 <= '0';
				init_done <= '0';
				if(i = 2000) then
					init_state<=done;
					i <= 0;
				else
					init_state<=eight;
					i <= i + 1;
				end if;
			when done =>
				init_state <= done;
				init_done <= '1';
			
		end case;
	end if;
end process power_on_initialize;
end Behavioral;